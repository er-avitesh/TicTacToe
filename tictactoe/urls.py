"""tictactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# import player
from .views import welcome
# from player.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'welcome', welcome),
    # path('player/home', player.views.home)
    url(r'^player/', include('player.urls')),
    url(r'^games/', include('gameplay.urls')),
    url(r'^$', welcome, name="tictactoe_home"),
]
