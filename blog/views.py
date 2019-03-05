from django.shortcuts import render , get_object_or_404 ,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post
from .form import PostBlog
# Create your views here.
def home(request):
    posts=Post.objects
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3)
    page=request.GET.get('page')
    blogs=paginator.get_page(page)
    return render(request,'home.html',{'posts':posts, 'blogs':blogs})

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

def blogpost(request):
    if request.method=="POST":
        form=PostBlog(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')


    else:
        form=PostBlog()
        return render(request,'new.html',{'form':form})    