from ads.models import Response


def counters(request):
    if request.user.is_authenticated:
        return {
            'user_responses': Response.objects.filter(ad__author=request.user)
        }
    return request
