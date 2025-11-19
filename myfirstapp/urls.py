from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('time/',views.time_view,name='time_view'),
    path('list_view/',views.list_view,name='list_view'),
]