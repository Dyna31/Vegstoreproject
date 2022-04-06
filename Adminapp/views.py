from django.shortcuts import render
from django.shortcuts import redirect
from Adminapp.models import categorydb
from Adminapp.models import productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Userviewapp.models import *

def index(request):
    ucount=productdb.objects.all().count()
    ucount1=Regidb.objects.all().count()
    ucount2=Cartdb.objects.all().count()
    ucount3=Contactdb.objects.all().count()
    return render(request, 'index.html',{'ucount':ucount,'ucount1':ucount1,'ucount2':ucount2,'ucount3':ucount3})
def add(request):
    return render(request,'add_category.html')
def getdata(request):
    if request.method == 'POST':
        img_a=request.FILES['abc']
        name_a=request.POST.get('name')
        description_a=request.POST.get('description')
        data=categorydb(name=name_a,description=description_a,abc=img_a)
        data.save()
    return redirect('add')

def viewcat(request):
    obj = categorydb.objects.all()
    return render(request,'view_category.html',{'obj':obj})

def addpro(request):
    categ = categorydb.objects.all()
    return render(request, 'add_product.html',{'categ':categ})

def adlogin(request):
    return render(request, 'login.html')

def getlogin(request):
    username_a=request.POST.get('username')
    password_a=request.POST.get('password')
    print(username_a)
    print(password_a)
    if User.objects.filter(username__contains=username_a).exists():
        user=authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            request.session['username'] = username_a
            request.session['password'] = password_a
            print(user)
            return redirect('index')
        else:
            return redirect('adlogin')
    else:
        return redirect('adlogin')
def getpro(request):
    if request.method =='POST':
         img_a=request.FILES['img']
         proname_a=request.POST.get('productname')
         category_a=request.POST.get('category')
         weight_a=request.POST.get('weight')
         price_a=request.POST.get('price')
         data=productdb(productname=proname_a,category=category_a,weight=weight_a,price=price_a,img=img_a)
         data.save()
    return redirect('viewpro')
def viewpro(request):
    obj = productdb.objects.all()
    return render(request, 'view_product.html',{'obj':obj})
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('adlogin')
def edit(request,id):
    obj = productdb.objects.filter(id=id)
    return render(request, 'edit.html',{'obj':obj})
def update(request,id):
    if request.method == 'POST':
        proname_c=request.POST.get('productname')
        category_c=request.POST.get('category')
        weight_c=request.POST.get('weight')
        price_c=request.POST.get('price')
        
        try:
            img_c=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=id).img  
    productdb.objects.filter(id=id).update(productname=proname_c,category=category_c,weight=weight_c,price=price_c,img=file)
    return redirect('viewpro')

def delete(request,id):
    productdb.objects.get(id=id).delete()
    return redirect('viewpro')




