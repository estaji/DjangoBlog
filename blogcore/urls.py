from django.urls import path
from .views import home, detail, category, api

app_name = "blog"
urlpatterns = [
    path('', home, name="home"),
    path('page/<int:page>', home, name="home"),
    path('article/<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('api',api, name="api"),
]
