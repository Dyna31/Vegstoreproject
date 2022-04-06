from django.urls import path
from.import views
urlpatterns=[
    path('',views.user,name='user'),
    path('regi',views.regi,name='regi'),
    path('shop/<str:catpro>/',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('getregi',views.getregi,name='getregi'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('userlogin1',views.userlogin1,name='userlogin1'),
    path('getcontact',views.getcontact,name='getcontact'),
    path('contactview',views.contactview,name='contactview'),
    path('singleproduct/<int:id>/',views.singleproduct,name='singleproduct'),
    path('cartdata/<int:id>/',views.cartdata,name='cartdata'),
    path('cart',views.cart,name='cart'),
    path('getcheckout',views.getcheckout,name='getcheckout'),
    path('checkout',views.checkout,name='checkout'),
    path('dele/<int:id>/',views.dele,name='dele'),
    path('cartview',views.cartview,name='cartview'),
    path('userlogout',views.userlogout,name='userlogout')
    ]
