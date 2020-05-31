from django.conf.urls import url
from django.urls import path
from egarbage import views
from django.contrib.auth import views as auth_views


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
    path('logout', views.logout, name='logout'),
    path('change-password/',
         auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),),
]

