"""
Routes for the subscriber API.
"""


def unsubscribe(request):
    """
    """

    data = {
    }

    return render(request, 'app.html', {
        'data': data,
        'title': 'Unsubscribe :('
    })