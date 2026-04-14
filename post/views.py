from django.shortcuts import render, redirect

from post.models import Post


def post_list(request):
    clubs = Post.objects.all()
    return render(request, "/list.html" , {'clubs': clubs})

def post_create(request):
    if request.method == "POST":
        # name = request.POST.get("name")
        # description = request.POST.get("description")
        # founded_year = request.POST.get("founded_year")

        title = request.POST.get("title")
        content = request.POST.get("content")
        if title:
            Post.objects.create(
                title=title,content=content
            )
        else:
           error = "Error"
           return render(request, "club/create.html" , {"error": error})
        return render(request, "club/create.html")






