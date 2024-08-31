"""
URL configuration for home_work project.

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
from blog.views import article_id, comment, create, delete, login, logout, main, myfeed, profile, register, set_password, topics, topics_id, topics_id_subscribe, topics_id_unsubscribe, update
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", main),
    path('my-feed/', myfeed),
    path('<article_id>/', article_id),
    path('<article_id>/comment', comment),
    path('<article_id>/update', update),
    path('<article_id>/delete', delete),
    path('create/', create),
    path('topics/', topics),
    path('topics/<topic_id>/',topics_id ),
    path('topics/<topic_id>/subscribe/', topics_id_subscribe),
    path('topics/<topic_id>/unsubscribe/', topics_id_unsubscribe),
    path('profile/', profile),
    path('register/', register),
    path('set-password/', set_password),
    path('login/', login),
    path('logout/', logout),
    path('admin/', admin.site.urls),
]
