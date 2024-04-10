from django.urls import path

from . import views


def asd():
    pass



app_name = 'about'

urlpatterns = [
    path('', views.description, name='description'),
]
