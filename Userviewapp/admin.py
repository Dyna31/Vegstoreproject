from django.contrib import admin
from .models import Regidb
admin.site.register(Regidb)
from .models import Contactdb
admin.site.register(Contactdb)
from .models import Cartdb
admin.site.register(Cartdb)
from .models import Checkoutdb
admin.site.register(Checkoutdb)

# Register your models here.
