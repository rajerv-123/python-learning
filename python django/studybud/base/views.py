from django.shortcuts import render


rooms = [
    {"id": 1, "name": "lets learn python"},
    {"id": 2, "name": "design with pip  learn python"},
    {"id": 3, "name": "frontend developer learn python"},
]

#  Create your views here.


def home(request):
    context = {"room": rooms}
    return render(request, "Home.html", context)


def room(request):
    return render(request, "Room.html")
