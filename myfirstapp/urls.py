from . import views
from django.urls import path,re_path

urlpatterns=[
    path('',views.home,name='home'),
    path('time/',views.time_view,name='time_view'),
    path('list_view/',views.list_view,name='list_view'),
    path('mylist/',views.MyList.as_view(),name='mylist'),
    path('items/',views.ItemListView.as_view(),name='item_list'),
]