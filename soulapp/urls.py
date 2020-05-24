from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='soulapp'),
    path('search/', views.search, name='search'),
    path('research/', views.research, name='research'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
