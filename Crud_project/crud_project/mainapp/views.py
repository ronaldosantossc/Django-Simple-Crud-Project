from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request,'apps/index.html', context)

def add_item(request):
    if request.method=="POST":
        name = request.POST['name']
        description = request.POST['description']
        item = Item(name = name,description = description)
        item.save()
        messages.info(request,"Item Added Sucessfully")

    else:
        pass    

    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request,'apps/index.html', context)

def delete_item(request, myid):
    item = Item.objects.get(id = myid)
    if request.method == "POST":
        item.delete()
        messages.info(request,"ITEM DELETED SUCESSFULLY")
        return redirect('/')
        
    context = {'item':item}
    return render(request, 'apps/delete.html', context)
 

def update_item(request, myid):
    if request.method == 'POST':
        item = Item.objects.get(id=myid)
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('index')
    
    context = {'item':item}
    
    return render(request, 'apps/update.html', context)