from django.contrib import admin
from .models import categorydb
admin.site.register(categorydb)
from .models import productdb
admin.site.register(productdb)

# Register your models here.
