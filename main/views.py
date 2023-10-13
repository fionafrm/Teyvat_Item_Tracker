import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
#Untuk main
def show_main(request):
    items = Item.objects.filter(user=request.user)

    if request.method == "POST":
        action = request.POST.get('action')
        item_id = request.POST.get('item_id')
        item = Item.objects.get(id=item_id)

        if action == "increase":
            item.amount += 1
            item.save()
        elif action == "decrease" and item.amount > 0:
            item.amount -= 1
            item.save()
        elif action == "remove":
            item.delete()
            items = Item.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'items' : items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

#Untuk create Item
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

#Untuk menampilkan data
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#Untuk daftar
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun kamu telah berhasil dibuat!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

#Untuk autentikasi
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Maaf, username atau password salah. Mohon coba lagi.')
    context = {}
    return render(request, 'login.html', context)

#Untuk logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

#Untuk ngambil data dengan json
def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item))

#Untuk edit Item
def edit_item(request, id):
    # Ngambil item dari id
    item = Item.objects.get(pk = id)

    # Set Item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

#Pake AJAX
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        user = request.user

        new_item= Item(name=name, price=price, description=description, amount=amount, category=category, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()