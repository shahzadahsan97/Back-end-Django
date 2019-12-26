from django.shortcuts import render
from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url +'">'+ album.album_title + '</a><br>'
    return HttpResponse(html)


def details(requset , album_id):
    return HttpResponse("<h2>Details for album id is:" + str(album_id) + "</h2>")

# Create your views here.
