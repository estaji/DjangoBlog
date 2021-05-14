from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article, Category

#def home(request, page=1):
#
#    articles_list = Article.objects.published()
#    paginator = Paginator(articles_list, 4)
#    articles = paginator.get_page(page)
#
#    context = {
#        "articles": articles,
#    }

#    return render(request, "blog/home.html", context)
class ArticleList(ListView):
    queryset = Article.objects.published()
    template_name = "blog/home.html"
    context_object_name = "articles"
    paginate_by = 4

def detail(request, slug):

    context = {
        "article": get_object_or_404(Article, slug=slug, status="p"),
    }

    return render(request, "blog/detail.html", context)

def category(request, slug, page=1):

    category = get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 4)
    articles = paginator.get_page(page)
    context = {
        "category": category,
        "articles": articles,
    }

    return render(request, "blog/category.html", context)

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