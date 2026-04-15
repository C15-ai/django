from django.shortcuts import render, redirect
from .forms import CountryForm
from .models import Country


def country_list(request):
    countries = Country.objects.all()
    return render(request, "country/country_list.html", {'countries': countries})


def country_create(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm()

    return render(request, 'country/country_create.html', {'form': form})
def country_update(request,pk=None):
    countries = Country.objects.filter(id=pk).first()
    form = CountryForm(instance=countries,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('country_list')
    return render(request, 'country/country_update.html',{'form':form, 'countries':countries})

def country_delete(request, pk=None):
    Country.objects.filter(id=pk).delete()
    return redirect('country_list')