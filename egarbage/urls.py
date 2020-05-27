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
]
