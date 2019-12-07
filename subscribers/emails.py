from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

class SubscriberEmails():
    def send_request_confirmation_email(email, token):
        context = {
            'url': settings.HOST_URL + '/api/subscribers/confirm/' + token
	    }

        html_content = render_to_string('emails/subscription-request.html', context)

        send_mail('Please confirm your subscription to ITR',
			html_content,
			'Intro To Rhythm <info@introtorhythm.com>',
			[email],
			fail_silently=True,
			html_message=html_content)


