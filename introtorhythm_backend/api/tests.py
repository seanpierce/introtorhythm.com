from datetime import timedelta
from unittest.mock import patch

import pytz
from django.core.cache import cache
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from content.models import About, MarqueeText
from schedule.models import Show


PACIFIC = pytz.timezone("America/Los_Angeles")


class FixedDateTime:
    """
    Minimal datetime replacement used to make content endpoint tests deterministic.

    The content view imports ``datetime`` directly, so patching that symbol with
    this class lets tests control both naive and timezone-aware calls to
    ``datetime.now()`` without changing production code.
    """

    fixed_now = None

    @classmethod
    def now(cls, tz=None):
        """Return the frozen time in the requested timezone, if one is provided."""
        if tz:
            return cls.fixed_now.astimezone(tz)
        return cls.fixed_now


class ContentEndpointTests(TestCase):
    """Tests for the public content endpoint used by the frontend homepage."""

    def setUp(self):
        # The endpoint is cached for normal requests, so each test starts clean.
        cache.clear()
        self.client = APIClient()

    def tearDown(self):
        # Clear again so a test response cannot leak into another test class.
        cache.clear()

    def test_get_content_returns_marquee_about_current_show_and_upcoming_shows(self):
        """
        The content endpoint should combine CMS text with live schedule context.

        This verifies the response includes active marquee text, about content,
        the currently airing show, and a Pacific-time listing for upcoming shows.
        """
        now = timezone.localtime()
        upcoming_start = now + timedelta(hours=3)

        # Only active marquee text should appear in the generated marquee string.
        MarqueeText.objects.create(content="Station news", active=True)
        MarqueeText.objects.create(content="Inactive news", active=False)
        About.objects.create(info="<p>About Intro to Rhythm</p>")

        # The model pre-save hook derives start/end datetimes from date/start_time.
        current_show = Show.objects.create(
            title="Live Now",
            info="Current show",
            date=now.date(),
            start_time=now.hour,
            duration=2,
            active=True,
        )
        upcoming_show = Show.objects.create(
            title="Later Set",
            info="Upcoming show",
            date=upcoming_start.date(),
            start_time=upcoming_start.hour,
            duration=1,
            active=True,
        )

        # Freeze the view's clock so the current/upcoming split is predictable.
        FixedDateTime.fixed_now = now

        with patch("api.views.content.datetime", FixedDateTime):
            response = self.client.get(reverse("get_content"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["about"], {"info": "<p>About Intro to Rhythm</p>"})

        # The endpoint returns a single display-ready string for the marquee UI.
        marquee_text = response.data["marqueeText"]
        upcoming_time = upcoming_show.start_date_time.astimezone(PACIFIC).strftime(
            "%I:%M %p"
        )
        timezone_label = now.astimezone(PACIFIC).strftime("%Z")

        self.assertIn("Station news", marquee_text)
        self.assertIn(f"Now Playing: {current_show.title}", marquee_text)
        self.assertIn(
            f"Coming Up: {upcoming_show.title} at {upcoming_time} {timezone_label}",
            marquee_text,
        )
        self.assertNotIn("Inactive news", marquee_text)
        self.assertEqual(marquee_text[-3:], " | ")

    def test_get_content_returns_empty_marquee_and_null_about_without_records(self):
        """
        The content endpoint should still return a stable shape when CMS data is absent.

        The frontend can rely on the same keys even before marquee/about records
        have been created in the admin.
        """
        FixedDateTime.fixed_now = timezone.localtime()

        with patch("api.views.content.datetime", FixedDateTime):
            response = self.client.get(reverse("get_content"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"marqueeText": " | ", "about": None})


@override_settings(INTERNAL_API_KEY="test-api-key")
class ScheduleEndpointTests(TestCase):
    """Tests for internal schedule maintenance endpoints and their API key guard."""

    def setUp(self):
        self.client = APIClient()

    @patch("api.views.schedule.run_pre_recorded_show_scheduler")
    def test_initiate_show_requires_valid_internal_api_key(self, scheduler_mock):
        """
        The initiate-show endpoint should reject unauthenticated internal calls.

        The scheduler service must not run unless the request includes the
        expected ``X-API-Key`` header.
        """
        response = self.client.post(reverse("initiate_show"))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        scheduler_mock.assert_not_called()

    @patch("api.views.schedule.run_pre_recorded_show_scheduler")
    def test_initiate_show_returns_scheduler_result_for_authenticated_request(
        self,
        scheduler_mock,
    ):
        """
        Authenticated initiate-show calls should proxy the scheduler result.

        The view is intentionally thin, so the test patches the scheduler service
        and verifies that its response becomes the API response body.
        """
        scheduler_mock.return_value = {
            "started": True,
            "show_id": 12,
            "audio": "episode.mp3",
            "config": "/tmp/scheduler.xml",
        }

        response = self.client.post(
            reverse("initiate_show"),
            HTTP_X_API_KEY="test-api-key",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, scheduler_mock.return_value)
        scheduler_mock.assert_called_once_with()

    @patch("api.views.schedule.cleanup_old_pre_recorded_shows")
    def test_cleanup_pre_recorded_shows_returns_cleanup_result_for_authenticated_request(
        self,
        cleanup_mock,
    ):
        """
        Authenticated cleanup calls should return the cleanup service summary.

        This keeps endpoint coverage focused on authentication and response
        behavior while leaving file deletion behavior to service-level tests.
        """
        cleanup_mock.return_value = {
            "deleted_count": 1,
            "deleted": [{"show_id": 4, "file": "old-show.mp3"}],
        }

        response = self.client.post(
            reverse("cleanup_pre_recorded_shows"),
            HTTP_X_API_KEY="test-api-key",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, cleanup_mock.return_value)
        cleanup_mock.assert_called_once_with()

    @patch("api.views.schedule.cleanup_old_pre_recorded_shows")
    def test_cleanup_pre_recorded_shows_requires_valid_internal_api_key(
        self,
        cleanup_mock,
    ):
        """
        Cleanup should reject requests with an invalid internal API key.

        A rejected request must not call into the cleanup service, since that
        service can delete uploaded audio files.
        """
        response = self.client.post(
            reverse("cleanup_pre_recorded_shows"),
            HTTP_X_API_KEY="wrong-key",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        cleanup_mock.assert_not_called()
