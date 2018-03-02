from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def post_comment(request):
    data = request.POST
    print(data)
    return HttpResponse('ok')