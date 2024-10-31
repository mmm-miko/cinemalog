from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import WatchList
from .forms import WatchListForm


# Create your views here.

def watchlist_view(request):
    watchlist_items = WatchList.objects.all()
    return render(request, "watchlist_list.html", {"watchlist_items": watchlist_items})

class WathListView(LoginRequiredMixin,ListView):
    model = WatchList

def create_watchlist(request):
    if request.method == "POST":
        form = WatchListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cinemalog/watchlist_list.html")  
    else:
        form = WatchListForm()
    return render(request, "create_watchlist.html", {"form": form})

class WatchListDetailView(DetailView):
    model = WatchList
    template_name = "detail_template.html"  
    context_object_name = "watchlist_item"
