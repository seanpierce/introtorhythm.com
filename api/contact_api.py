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
        return self.Response(payload)