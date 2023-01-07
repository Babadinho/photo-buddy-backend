from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getPhotos, name='photos'),
    path('products/<str:pk>', views.getPhoto, name='photo')
]
