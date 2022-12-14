from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import TodolistModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    model_todo = TodolistModel.objects.filter(user = request.user)
    context = {
    'list_todo': model_todo,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def show_newtask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TodolistModel.objects.create(title = title, description = description, date = datetime.date.today(), user = request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    return render(request, "createtask.html")

def show_json(request):
    model_todo = TodolistModel.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", model_todo), content_type="application/json")

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = TodolistModel.objects.create(title = title, description = description, date = datetime.date.today(), user = request.user)

        result = {
            'fields':{
                'title':todo.title,
                'date':todo.date,
                'description':todo.description,
            },
            'pk':todo.pk
        }
        return JsonResponse(result)