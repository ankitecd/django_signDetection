from django.urls import path

from . import recognize

urlpatterns = [
    path('', recognize.index, name='index'),
    path('click/', recognize.click, name='click'),   
]