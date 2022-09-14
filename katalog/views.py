from django.shortcuts import render
from katalog.models import CatalogItem
...
# TODO: Create your views here.

def show_katalog(request):
    item_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': item_catalog,
        'nama': 'Diona',
        'npm': 2106708255,
    }
    return render(request, "katalog.html", context)


