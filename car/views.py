from django.shortcuts import render , redirect

from .forms import CarForm

from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, "car/car_list.html", {'cars': cars})


def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'car/car_create.html', {'form': form})


def car_update(request, pk=None):
    cars = Car.objects.filter(id=pk).first()
    if request.method == "POST":
        form = CarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=cars)
    return render(request, 'car/car_update.html', {'form': form, 'cars': cars})
def car_delete(request, pk=None):
    Car.objects.filter(id=pk).delete()
    return redirect('car_list')