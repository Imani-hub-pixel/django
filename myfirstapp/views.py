from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.views import View
from .models import MyFirstModel
from django.views.generic.list import ListView

"""
The response can be an html page,a redirect to another url,an error i.e 404
JSON,XML,images or any browser-compatible content.
"""
# Create your views here.
def home(request):
    return HttpResponse("Welcome to my first django app")


def time_view(request):
    now=datetime.datetime.now()
    html="Time is {}".format(now)
    return HttpResponse(html)

def list_view(request):
    context={}
    context["dataset"]=MyFirstModel.objects.all()
    return render(request,"list_view.html",context)

class MyList(ListView):
    model=MyFirstModel
    template_name="mylist.html"

class ItemListView(View):
    def get(self,request):
        return HttpResponse("This is an item list view")
    
