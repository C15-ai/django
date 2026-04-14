from django.shortcuts import render, redirect

from product.models import Product



def product_list(request):
    product = Product.objects.all()
    return render(request, "product/product_list.html" , {'products': product})
def product_create(request,):
     if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")

        if name:
            Product.objects.create(
                name=name,description=description,price=price
            )
            return redirect('product_list')
        else:
            error = "Error"
            return render(request, "product/product_create.html", {"error": error})
     return render(request, "product/product_create.html")
def product_update(request, pk):
    product = Product.objects.filter(id=pk).first()
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.save()
        return redirect('product_list')
    return render(request, 'product/product_update.html', {'product': product})