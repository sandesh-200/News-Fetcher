from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="news_home"),
    path('news/', views.news, name="news_main")
]