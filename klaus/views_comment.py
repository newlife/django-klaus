from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import sh
from sh.contrib import git
from klaus.models import Repo, Comment
from django.conf import settings

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

@csrf_exempt
def clone_repo(request):
    data = request.POST
    print(data)
    repo_url = data['repo_url']
    repo_home = settings.REPO_HOME
    sh.cd(repo_home)
    git.clone(repo_url)
    return HttpResponse('ok')