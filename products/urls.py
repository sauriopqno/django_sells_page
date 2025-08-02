from django.urls import path
from . import views

app_name='productos'

urlpatterns = [

    path('',views.product_lists, name='list' ),
    path('<slug:slug>',views.product_page, name='page' ),
    
]