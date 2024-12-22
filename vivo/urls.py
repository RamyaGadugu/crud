from django.contrib import admin
from django.urls import path
from vivo import views
urlpatterns = [
    path('', views.index,name="index"),
    path('about',views.about,name="about"),
    path('insert',views.insertdata,name="insert"),
    path('update/<id>',views.updateData,name='update'),
    path('delete/<id>',views.delete,name='delete'),
]
