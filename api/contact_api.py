import json
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class SendBookingRequest(View):
    """
    Sends a booking request email from the website to the ITR booking account.
    """

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)

        template = get_template("emails/booking-request.html").render({
            'name': payload['name'],
            'djName': payload['djName'],
            'email': payload['email'],
            'proposal': payload['proposal'],
            'additional': payload['additional']
        })

        email = EmailMessage(
            f'Booking Request - {payload["name"]} - {payload["djName"]}', # subject
            template, # body
            f'Booking Request <{settings.EMAIL_HOST_USER}>', # from
            [settings.EMAIL_BOOKING_RECIPIENT], # to
            [settings.EMAIL_HOST_USER], # bcc
            reply_to=[payload["email"]] #reply-to
        )

        email.content_subtype = "html"
        email.send()

        return HttpResponse(json.dumps(None), content_type='application/json')