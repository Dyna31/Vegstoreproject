from django.db import models
from Adminapp.models import*


class Regidb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=False)
    email=models.CharField(max_length=100,null=True,blank=False)
    address=models.CharField(max_length=100,null=True,blank=False)
    password=models.CharField(max_length=100,null=True,blank=False)
class Contactdb(models.Model):
    nameu=models.CharField(max_length=100,null=True,blank=False)
    emailu=models.CharField(max_length=100,null=True,blank=False)
    subject=models.CharField(max_length=100,null=True,blank=False)
    message=models.CharField(max_length=100,null=True,blank=False)
class Cartdb(models.Model):
    productid=models.ForeignKey(productdb, on_delete=models.CASCADE,null=True,blank=False)
    userid=models.ForeignKey(Regidb, on_delete=models.CASCADE,null=True,blank=False)
    quantity=models.IntegerField(null=True,blank=False)
    total=models.IntegerField(null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)
class Checkoutdb(models.Model):
    cartid=models.ForeignKey(Cartdb, on_delete=models.CASCADE,null=True,blank=False)
    firstname=models.CharField(max_length=100,null=True,blank=False)
    lastname=models.CharField(max_length=100,null=True,blank=False)
    state=models.CharField(max_length=100,null=True,blank=False)
    streetaddress=models.CharField(max_length=100,null=True,blank=False)
    town=models.CharField(max_length=100,null=True,blank=False) 
    postcode=models.IntegerField(null=True,blank=False)
    phone=models.IntegerField(null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)








