# from django.shortcuts import render
from django.views.generic import ListView
from .models import WatchList

# Create your views here.

class WathListView(ListView):
    model = WatchList
