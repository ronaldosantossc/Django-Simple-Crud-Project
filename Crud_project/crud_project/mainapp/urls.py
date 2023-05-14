
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from mainapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add_item',views.add_item,name='additem'),
    path('deleteItem/<int:myid>/',views.delete_item,name='delete'),
    path('updateItem/<int:myid>/',views.update_item,name='update'),
]