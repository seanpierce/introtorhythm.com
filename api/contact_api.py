from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from . import APIView


class SendBookingRequest(APIView):
    """
    Sends a booking request email from the website to the ITR booking account.
    """

    def post(self, request, *args, **kwargs):
        payload = self.GetPayload(
            request, 
            ['name', 'djName', 'email', 'proposal', 'additional']
        )

        template = get_template("emails/booking-request.html").render({
            'name': payload['name'],
            'djName': payload['djName'],
            'email': payload['email'],
            'proposal': payload['proposal'],
            'additional': payload['additional']
        })

        email = EmailMessage(
            f'Booking Request - {payload["name"]} - {payload["djName"]}',
            template,
            f'Booking Request <{settings.EMAIL_HOST_USER}>',
            [settings.EMAIL_BOOKING_RECIPIENT],
            [settings.EMAIL_HOST_USER],
            reply_to=[payload["email"]]
        )

        email.content_subtype = "html"
        email.send()

        return self.Response()