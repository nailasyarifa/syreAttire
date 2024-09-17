from django.shortcuts import render, redirect
from .models import ItemEntry 
from .forms import ItemEntryForm
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    items = ItemEntry.objects.all()  # Mengambil semua item dari database

    context = {
        'name': 'Your Name Here',  # Nama pengguna atau informasi lain
        'items': items,  # Daftar semua item pakaian
        
    }
    return render(request, 'main.html', context)


def create_items_entry (request):
    form = ItemEntryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items_entry.html", context)


def show_xml(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
