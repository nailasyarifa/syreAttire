from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()  # Mengambil semua item dari database
    context = {
        'items': items,
    }
    return render(request, 'main/item_list.html', context)
