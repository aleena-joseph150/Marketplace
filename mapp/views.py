import os

from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import *
from .models import *


def index(request):
    items=item.objects.filter(is_sold=False)[0:6]
    categories=category.objects.all()
    return render(request,'core/index.html',{'categories':categories,'items':items})

def contact(request):
    return render(request,'core/contact.html')


def signup(request):
    if 'username' is request.session:
        return redirect(dashboard)
    else:
        if request.method=='POST':
                un=request.POST['username']
                psw=request.POST['password']
                psw2=request.POST['password2']

                if psw==psw2:
                    if User.objects.filter(username=un).exists():
                        messages.info(request,"username already exists")
                        return redirect(signup)

                    else:
                        b=User.objects.create_user(username=un,password=psw)
                        b.save()
                        return redirect(login)
                else:
                    messages.info(request, "Password doesn't match")
                    return redirect(signup)

        return render(request,'core/signup.html')


def login(request):
    if request.method=='POST':
        a = logform(request.POST)
        if a.is_valid():
            uname = request.POST.get('username')
            psw = request.POST.get('password')
            user = auth.authenticate(username=uname, password=psw)
            if user is not None:
                request.session['username']=uname
                auth.login(request, user)
                return redirect(dashboard)
            else:
                messages.info(request, "invalid")
                return redirect(login)
    else:
        return render(request,'core/login.html')

def logout(request):
    auth.logout(request)
    return redirect(index)


def detail(request, pk):
    Item = get_object_or_404(item, pk=pk)
    related_items = item.objects.filter(category=Item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'core/detail.html', {
        'item': Item,
        'related_items': related_items
    })





def add(request):
    if 'username' is request.session:

        if request.method == 'POST':
            form = newitem(request.POST, request.FILES)

            if form.is_valid():
                item = form.save(commit=False)
                item.created_by = request.user
                item.save()

                return redirect(detail, pk=item.id)
        else:
            form = newitem()

        return render(request, 'logged/add.html', {
            'form': form,
            'title': 'New item'

        })
    else:
        return redirect(login)

def dashboard(request):
    items = item.objects.filter(created_by=request.user)

    return render(request, 'logged/dashboard.html', {
        'items': items,
    })


def delete(request, pk):
    items = get_object_or_404(item, pk=pk, created_by=request.user)
    items.delete()

    return redirect(dashboard)


def edititem(request,pk):
    prod=item.objects.get(pk=pk)
    a=str(prod.image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image=request.FILES['image']
        prod.iname=request.POST.get('iname')
        prod.des = request.POST.get('des')
        prod.price = request.POST.get('price')
        prod.save()
        return redirect(dashboard)
    context={'prod':prod,'a':a}

    return render(request,'logged/edit.html',context)