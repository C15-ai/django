from django.shortcuts import render ,redirect
from category.models import Category


def category_list(request):
    categories = Category.objects.all()
    return render(request, "category/category_list.html", {'categories': categories})


def category_create(request, ):
    if request.method == "POST":
        name = request.POST.get("name")
        year = request.POST.get("year")


        if name:
            Category.objects.create(
                name=name, year=year
            )
            return redirect('category_list')
        else:
            error = "Error"
            return render(request, "category/category_create.html", {"error": error})
    return render(request, "category/category_create.html")

def category_update(request, pk):
    category = Category.objects.filter(id=pk).first()
    if request.method == "POST":
        category.name = request.POST.get("name")
        category.year = request.POST.get("year")

        category.save()
        return redirect('category_list')
    return render(request, 'category/category_update.html', {'category': category})
def category_delete(request, pk=None):
    Category.objects.filter(id=pk).delete()
    return redirect('category_list')