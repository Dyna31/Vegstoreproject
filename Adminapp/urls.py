from django.urls import path
from.import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('getdata',views.getdata,name='getdata'),
    path('viewcat',views.viewcat,name='viewcat'),
    path('addpro',views.addpro,name='addpro'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('getlogin',views.getlogin,name='getlogin'),
    path('viewpro',views.viewpro,name='viewpro'),
    path('getpro',views.getpro,name='getpro'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]