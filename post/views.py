from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from comment.models import Comment
from .models  import Post
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


@login_required
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title:
            Post.objects.create(title=title,content=content,author=request.user)
            return redirect('post_list')
        else:
            error = "Post name is required"
            return render(request, "post/post_create.html", {"error": error})
    return render(request, "post/post_create.html")


def post_detail(request, id):
    post = Post.objects.filter(id=id).first()
    return render(request, 'post/post_detail.html', {"posts": post})

@login_required
def post_delete(request , id):
    p1 = Post.objects.filter(id=id).first()
    p1.delete()
    return redirect('post_list')

@login_required
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(post=post, user=request.user, text=content)
            return redirect('post_detail', id=id)
        else:
            error = "Comment yozish kerak"
            return render(request, "post/post_detail.html", {"posts": post, "error": error})
    return redirect('post_detail', id=id)