from django.http import HttpResponse
from django.shortcuts import render, redirect

from club.models import Club

def club_list(request):
    clubs = Club.objects.all()
    return render(request, "club/list.html" , {'clubs': clubs})
def club_detail(request , pk):
    clubs =  Club.objects.filter(id=pk).first()
    return render(request, 'club/detail.html',{"clubs":clubs})


def club_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        founded_year = request.POST.get("founded_year")

        if name:
            Club.objects.create(
                name=name,description=description,founded_year=founded_year
            )
            return redirect('club_list')
        else:
            error = "Club name is required"
            return render(request, "club/create.html", {"error": error})


    return render(request, "club/create.html")

def club_update(request, pk):
    club = Club.objects.filter(id=pk).first()
    if request.method == "POST":
        club.name = request.POST.get("name")
        club.description = request.POST.get("description")
        club.founded_year = request.POST.get("founded_year")
        club.save()
        return redirect('club_list')
    return render(request, 'club/update.html', {'club': club})

def club_delete(request, pk=None):
    Club.objects.filter(id=pk).delete()
    return redirect('club_list')




