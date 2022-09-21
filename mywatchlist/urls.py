from django.urls import path
from mywatchlist.views import show_mywatchlist, show_watchlink, show_xml, show_json


app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlink, name='show_watchlink'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]