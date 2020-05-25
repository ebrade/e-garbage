from django.urls import path

from egarbage import views

# The application urls in the /hello directory to be renamed in coming versions.
urlpatterns = [
    path("", views.home, name='about'),
    path("home/", views.home, name='login'),
    path("about/", views.about, name='about'),
    path("history/", views.history, name='history'),
    path("register/", views.register, name='register'),

]
