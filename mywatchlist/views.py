
from django.shortcuts import render
from mywatchlist.models import MovieWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_movie = MovieWatchlist.objects.all()
    context = {
        'list_movie': data_movie,
        'name': 'Diona Varastika',
        'npm': '2106708255'
    }
    return render(request, "mywatchlist.html", context)

def show_watchlink(request):
    context = {
        'name': 'Diona Varastika',
        'npm': '2106708255'
    }
    return render(request, "watchlink.html", context)

def show_xml(request):
    data = MovieWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MovieWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

