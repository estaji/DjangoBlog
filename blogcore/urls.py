from django.urls import path
from .views import home, detail, api

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('article/<slug:slug>', detail, name="detail"),
    path('api',api, name="api"),
]
