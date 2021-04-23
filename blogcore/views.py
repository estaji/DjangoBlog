from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def home(request):

    context = {
        "username": "Omid",
        "age": "28",
        "job": "DevOps",
        "articles": Article.objects.filter(status='p').order_by('-publish')
    }

    return render(request, "blog/home.html", context)

def detail(request, slug):

    context = {
        "article": Article.objects.get(slug=slug)
    }

    return render(request, "blog/single.html", context)

def api(request):

    apidata = {
        "1": {
            "title": "Article One",
            "id": "10",
            "slug": "first-article",
        },
        "2": {
            "title": "Article Two",
            "id": "11",
            "slug": "second-article",
        },
        "3": {
            "title": "Article Three",
            "id": "12",
            "slug": "third-article",
        }
    }

    return JsonResponse(apidata)