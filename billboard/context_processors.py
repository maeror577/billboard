from ads.models import Response


def counters(request):
    return {
        'user_responses': Response.objects.filter(ad__author=request.user)
    }
