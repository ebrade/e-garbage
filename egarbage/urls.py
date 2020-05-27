from django.urls import path

from egarbage import views

# The application urls in the /hello directory to be renamed in coming versions.
urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('register/', views.register, name='register'),
    path('add/', views.RegisterItem.as_view(), name='add_new_item'),
    path('load_district', views.load_district, name='load_district'),
    path('load_sector', views.load_sector, name='load_sector'),
    path('load_cell', views.load_cell, name='load_cell'),
    path('load_village', views.load_village, name='load_village'),

]
