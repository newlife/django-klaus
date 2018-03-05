from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from klaus.models import Repo, Comment

@csrf_exempt
def post_comment(request):
    data = request.POST
    path = data['path']
    repo = Repo.objects.get(id=1)
    line = data['line']
    text = data['text']
    rev = data['rev']
    Comment.objects.create(repo = repo,file_path=path,rev=rev,line=line,content=text)
    return HttpResponse('ok')