from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import ItemEntry 
from .forms import ItemEntryForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')

def show_main(request):
  
    context = {
        'name': request.user.username,  #tugas 4
        'last_login': request.COOKIES['last_login'], # Tambahkan last_login ke context
    }
    return render(request, 'main.html', context)


def create_items_entry (request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        item_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items_entry.html", context)

@csrf_exempt
@require_POST
def add_items_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    category = strip_tags(request.POST.get("category"))
    size = strip_tags(request.POST.get("size"))
    color = strip_tags(request.POST.get("color"))
    price = strip_tags(request.POST.get("color"))
    user = request.user

    new_item = ItemEntry(
        name=name, category=category,
        size=size, color=color, 
        price=price,
        user=user
    )
    new_item.save()

    return HttpResponse(b"CREATED", status=201)


def show_xml(request):
    data = ItemEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register (request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else: 
          messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request,id):
    category = ItemEntry.objects.get(pk = id)
    form = ItemEntryForm(request.POST or None, instance=category)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form' : form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    # Get item berdasarkan id
    category = ItemEntry.objects.get(pk = id)
    # Hapus item
    category.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
    
