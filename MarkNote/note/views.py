from django.shortcuts import render , get_object_or_404 ,redirect
from .models import Note
from .forms import CommentForm ,CreateBlog
from django.core.paginator import Paginator
# Create your views here.
def post_list(request):
    posts = Note.published.all()
    paginator = Paginator(posts, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"blog/post/list.html",{"page_obj": page_obj})

def post_detail(request,slug,day,year,month):
    post = get_object_or_404(Note,publish__year=year,publish__month=month,publish__day=day,slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect("blog:post_detail",slug=post.slug,year=post.publish.year,month=post.publish.month,day=post.publish.day)
        else:
            print("form is not valid")
    else:
        form = CommentForm()
    
    comment = post.comments.all()
    return render(request,"blog/post/detail.html",{"post":post,"form":form,"comment":comment})

def create_post(request):
    if request.method == "POST":
        form = CreateBlog(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect("blog:post_list")
        else:
            print("form not valid")
    else:
        form = CreateBlog()
    return render(request,"blog/post/form.html",{"form":form})

def show_my_post(request):
    post = Note.published.all().filter(author=request.user)
    return render(request,"blog/post/my_post.html",{"post":post})