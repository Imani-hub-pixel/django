from django.urls import path
from . import views

urlpatterns = [
    path('simple/',views.simple_view,name='simple_view'),
    path('check_age/',views.check_age,name='check_age'),
    path('loop/',views.loop,name='loop'),
]