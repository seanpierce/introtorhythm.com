from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    throttle_classes,
)

@api_view(["GET"])
@authentication_classes([])
@throttle_classes([])
def initiate_show(request):
    """
    Checks for a show that is scheduled to begin at this time. 
    If one exists, recreate the schedule show XMl config file for the schedule icecast process. 
    """
    pass