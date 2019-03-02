from django.shortcuts import render , get_object_or_404 ,redirect
from django.utils import timezone
from .models import Post
# Create your views here.
def home(request):
    posts=Post.objects
    return render(request,'home.html',{'posts':posts})

def detail(request,id):
    post=get_object_or_404(Post,pk=id)
    return render(request,'detail.html',{'post':post})   

def new(request):
    return render(request,'new.html')    

def create(request):
    post=Post()
    post.title=request.GET['title']
    post.body=request.GET['body']
    post.pubdate=timezone.datetime.now()
    post.save()
    return redirect('/detail/'+str(post.id))

