from django.shortcuts import render
from django.shortcuts import redirect
from Userviewapp.models import Regidb
from Userviewapp.models import Contactdb
from Userviewapp.models import  Cartdb
from Userviewapp.models import Checkoutdb

from django.db.models.aggregates import Sum

from Adminapp.models import *
def user(request):
    u=request.session.get('userid')
    data=categorydb.objects.all()
    obj=productdb.objects.all()
    cartcount=Cartdb.objects.filter(userid=u,status=0).count()
    return render(request, 'user.html',{'obj':obj,'cartcount':cartcount,'data':data})

def regi(request):
    return render(request,'registration1.html')

def shop(request,catpro):
    if(catpro == "all"):
        data=productdb.objects.all()
    else:
        data = productdb.objects.filter(category=catpro)
    u=request.session.get('userid')
   
    cartcount=Cartdb.objects.filter(userid=u,status=0).count()
    return render(request,'shop.html',{'cartcount':cartcount,'data':data})

def about(request):
    u=request.session.get('userid')
    cartcount=Cartdb.objects.filter(userid=u,status=0).count()
    return render(request,'about.html',{'cartcount':cartcount})
def contact(request):
    u=request.session.get('userid')
    cartcount=Cartdb.objects.filter(userid=u,status=0).count()
    return render(request, 'contact.html',{'cartcount':cartcount})

def getregi(request):
     if request.method == 'POST':
         username_a=request.POST.get('username')
         email_a=request.POST.get('email')
         address_a=request.POST.get('address')
         password_a=request.POST.get('password')
         data=Regidb(username=username_a,email=email_a,address=address_a,password=password_a)
         data.save()
     return redirect('loginuser')
def loginuser(request):
    return render(request, 'login1.html')
def userlogin1(request):
    username_a=request.POST.get('username')
    password_a=request.POST.get('password')
    if Regidb.objects.filter(username=username_a,password=password_a).exists():
        data=Regidb.objects.filter(username=username_a,password=password_a).values('email','address','id').first()
        request.session['email']=data['email']
        request.session['address']=data['address']
        request.session['userid']=data['id']
        request.session['username_a']=username_a
        request.session['password_a']=password_a
        return redirect('user')
    else:
        return render(request, 'login1.html',{'msg':'Invalid User Credentials'})

def getcontact(request):
    if request.method=='POST':
        name_x=request.POST.get('nameu')
        email_x=request.POST.get('emailu')
        subject_x=request.POST.get('subject')
        message_x=request.POST.get('message')
        data=Contactdb(nameu=name_x,emailu=email_x,subject=subject_x,message=message_x)
        data.save()
    return redirect('contact')

def contactview(request):
    obj = Contactdb.objects.all()
    return render(request,'contact_tableview.html',{'obj':obj})
    
def checkout(request):
    u=request.session.get('userid')
    obj=Cartdb.objects.filter(userid=u,status=0)
    s = Cartdb.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request, 'checkout.html',{'obj':obj,'s':s})

def singleproduct(request,id):
    obj=productdb.objects.filter(id=id)
    return render(request, 'singleproduct.html',{'obj':obj})

def cartdata(request,id):
    if 'userid' in request.session:
        quantity=request.POST.get('quantity')
        total=request.POST.get('total')
        userid=request.POST.get('id')
        data=Cartdb(productid=productdb.objects.get(id=id),quantity=quantity,total=total,userid=Regidb.objects.get(id=userid),status=0)
        data.save()
        print(userid)
    return redirect('cart')

def cart(request):
    u=request.session.get('userid')
    obj=Cartdb.objects.filter(userid=u,status=0)
    cartcount=Cartdb.objects.filter(userid=u,status=0).count()
    return render(request,'cart.html',{'obj':obj,'cartcount':cartcount})
    
def getcheckout(request):
    if request.method=='POST':
        firstname_a=request.POST.get('firstname')
        lastname_a=request.POST.get('lastname')
        state_a=request.POST.get('state')
        streetaddress_a=request.POST.get('streetaddress')
        town_a=request.POST.get('town')
        post_a=request.POST.get('postcode')
        phone_a=request.POST.get('phone')
        u=request.session.get('userid')
        order=Cartdb.objects.filter(userid=u,status=0)
        print(order)
        for i in order:
            data=Checkoutdb(cartid=Cartdb.objects.get(id=i.id),firstname=firstname_a,lastname=lastname_a,state=state_a,streetaddress=streetaddress_a,town=town_a,postcode=post_a,phone=phone_a)
            data.save()
            Cartdb.objects.filter(id=i.id).update(status=1)
    return redirect('user')

def dele(request,id):
   Cartdb.objects.get(id=id).delete()
   return redirect('cart')

def cartview(request):
    obj = Cartdb.objects.all()
    a = Checkoutdb.objects.all()
    return render(request,'ordersview.html',{'obj':obj,'a':a})

def userlogout(request):
    del request.session['username_a']
    del request.session['email']
    del request.session['address']
    del request.session['password_a']
    return redirect('user')







    







