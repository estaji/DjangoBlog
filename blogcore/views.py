from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article, Category

def home(request):

    context = {
        "articles": Article.objects.filter(status='p'),
        "category": Category.objects.filter(status=True)
    }

    return render(request, "blog/home.html", context)

def detail(request, slug):

    context = {
        "article": get_object_or_404(Article, slug=slug, status="p"),
        "category": Category.objects.filter(status=True)
    }

    return render(request, "blog/detail.html", context)

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