from django.conf.urls import url
from django.urls import path

from egarbage import views

# Some urls below needs to be modified
from egarbage.views import signup

urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('register_item/', views.register_item, name='register_item'),
    path('add/', views.RegisterItem, name='add_new_item'),
    path('load_district', views.load_district, name='load_district'),
    path('load_sector', views.load_sector, name='load_sector'),
    path('load_cell', views.load_cell, name='load_cell'),
    path('load_village', views.load_village, name='load_village'),
    url(r'^signup/$', views.signup, name='signup'),
]
