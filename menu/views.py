from django.shortcuts import render,redirect
from . models import category,category_product,store
from django.contrib import messages

# Create your views here.
def index(request):
    categories=category.objects.filter(status=0)
    menu_view=category_product.objects.filter(new_arrival=0)
    store_detail=store.objects.all()
    return render(request,'index.html',context={'category':categories,'menu_view':menu_view,'store':store_detail})

def menu(request,slug):
    if (category.objects.filter(slug=slug,status=0)):
        menu_view=category_product.objects.filter(category__slug=slug)  
    else:
        messages.error(request,"No Such Category")
        return redirect('home')
    store_detail=store.objects.all()
    return render(request,'menu.html',{'menu_view':menu_view,'store':store_detail})