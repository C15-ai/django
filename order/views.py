from django.shortcuts import render, redirect

from order.forms import OrderForm
from order.models import Order


def order_list(request):
    orders = Order.objects.all()
    return render(request, "country/country_list.html", {'orders': orders})


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, 'order/order_create.html', {'form': form})

def country_update(request, pk=None):
    orders = Order.objects.filter(id=pk).first()

    if request.method == "POST":
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=orders)
    return render(request, 'order/order_update.html', {'form': form, 'orders': orders})
def country_delete(request, pk=None):
    Order.objects.filter(id=pk).delete()
    return redirect('order_list')