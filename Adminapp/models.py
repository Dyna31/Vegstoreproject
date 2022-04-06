from django.db import models
from django.core.validators import RegexValidator
alphaneumeric= RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class categorydb(models.Model):
    abc=models.ImageField(upload_to='media',null=True,blank=False)
    name=models.CharField(max_length=100,null=True,blank=False)
    description=models.CharField(max_length=500,null=True,blank=False)
# Create your models here.
class productdb(models.Model):
    img=models.ImageField(upload_to='media',null=True,blank=False)
    productname=models.CharField(max_length=100,null=True,blank=False)
    category=models.CharField(max_length=100,null=True,blank=False)
    weight=models.CharField(max_length=100,null=True,blank=True,validators=[alphaneumeric])
    price=models.IntegerField(null=True,blank=False)

