"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cinemalog.views import WathListView
from cinemalog.views import watchlist_view
from cinemalog.views import create_watchlist
from cinemalog.views import WatchListDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", WathListView.as_view(), name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("watchlist/", watchlist_view, name="watchlist_list"),
    path("watchlist/create/", create_watchlist, name="create_watchlist"),
    path("watchlist/<int:pk>/", WatchListDetailView.as_view(), name="watchlist_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)