from django.shortcuts import render
from django.http import HttpResponse
import random #this is imported from python


# Create your views here. The python codes run here. Render makes the visuals based on the html codes

def home(request):
    return render(request, "generator/home.html")

def password(request):
    thepassword = ""

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        characters.extend(list("!#¤%&/()=?"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    length = int(request.GET.get("length",12)) #grabs the selection

    for x in range(length):
        thepassword += random.choice(characters) #randomly picks characters from list

    return render(request, "generator/password.html", {"password":thepassword})

def about(request):
    return render(request, "generator/about.html")
