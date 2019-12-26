from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is a music app home page</h1>")

def details(requset , album_id):
    return HttpResponse("<h2>Details for album id is:" + str(album_id) + "</h2>")

# Create your views here.
