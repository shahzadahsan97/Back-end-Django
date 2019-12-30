from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
#from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request , 'index.html' , context)


def details(requset , album_id):
    return HttpResponse("<h2>Details for album id is:" + str(album_id) + "</h2>")

# Create your views here.
