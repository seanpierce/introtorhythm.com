from django.test import TestCase

from content.models import About, MarqueeText
from content.models.about import About as AboutModel
from content.models.marquee_text import MarqueeText as MarqueeTextModel


class MarqueeTextModelTests(TestCase):
    """Unit tests for the MarqueeText CMS model."""

    def test_marquee_text_stores_content_and_defaults_to_active(self):
        """
        New marquee text should be active unless an admin explicitly disables it.

        The active default matters because the content API only includes active
        marquee rows in the homepage marquee response.
        """
        marquee_text = MarqueeText.objects.create(
            content="Tonight: guest mixes and station news."
        )

        self.assertEqual(
            marquee_text.content,
            "Tonight: guest mixes and station news.",
        )
        self.assertTrue(marquee_text.active)

    def test_marquee_text_can_be_marked_inactive(self):
        """
        Admins should be able to keep a marquee row without publishing it.

        The model stores the inactive state directly so endpoint code can filter
        with a simple ``active=True`` lookup.
        """
        marquee_text = MarqueeText.objects.create(
            content="Draft announcement",
            active=False,
        )

        self.assertFalse(marquee_text.active)

    def test_marquee_text_string_representation_is_admin_friendly(self):
        """
        The string representation should identify the singleton-style admin row.

        This keeps relation labels and admin breadcrumbs predictable instead of
        exposing raw content text that can change frequently.
        """
        marquee_text = MarqueeText.objects.create(content="Station update")

        self.assertEqual(str(marquee_text), "Marquee Text")

    def test_marquee_text_allows_empty_content(self):
        """
        The content field is optional so admins can temporarily blank the marquee.

        This verifies the model-level ``blank``/``null`` behavior reflected in
        migrations and forms.
        """
        marquee_text = MarqueeText.objects.create()

        self.assertIsNone(marquee_text.content)

    def test_marquee_text_verbose_name_plural_matches_admin_label(self):
        """
        The admin uses a custom plural label for the singleton-style model.

        This test protects the label shown in Django admin navigation.
        """
        self.assertEqual(MarqueeText._meta.verbose_name_plural, "Marquee Text")


class AboutModelTests(TestCase):
    """Unit tests for the About CMS model."""

    def test_about_stores_html_info(self):
        """
        About content should preserve saved HTML for the frontend info section.

        The model uses TinyMCE's HTML field, so stored markup should round-trip
        through the ORM unchanged.
        """
        about = About.objects.create(info="<p>Independent radio from Oakland.</p>")

        self.assertEqual(about.info, "<p>Independent radio from Oakland.</p>")

    def test_about_allows_empty_info(self):
        """
        The info field is optional so the site can exist before copy is written.

        This mirrors the admin workflow where an About row may be created before
        final content is available.
        """
        about = About.objects.create()

        self.assertIsNone(about.info)

    def test_about_string_representation_is_admin_friendly(self):
        """
        The string representation should describe the admin-managed content row.

        This avoids displaying empty or long HTML content as the object label.
        """
        about = About.objects.create(info="<p>About the station.</p>")

        self.assertEqual(str(about), "Info / About")

    def test_about_verbose_name_plural_matches_admin_label(self):
        """
        The admin uses a custom plural label for the about/info singleton row.

        This test protects the label shown in Django admin navigation.
        """
        self.assertEqual(About._meta.verbose_name_plural, "Info / About")


class ContentModelPackageTests(TestCase):
    """Tests for the model package exports used by the rest of the project."""

    def test_models_package_exports_content_models(self):
        """
        Importing from ``content.models`` should expose both concrete model classes.

        Views, serializers, and admin code import through this package, so this
        small test catches accidental changes to ``models/__init__.py``.
        """
        self.assertIs(About, AboutModel)
        self.assertIs(MarqueeText, MarqueeTextModel)
