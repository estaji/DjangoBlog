from django.urls.base import set_urlconf
from django.views.generic import ListView#, DetailView
from account.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
#from account.mixins import AuthorAccessMixin
from django.http import JsonResponse
from .models import Article, ArticleHit, Category
from django.db.models import Count, Q
from datetime import datetime, timedelta

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
    #queryset = Article.objects.published()
    last_month = datetime.today() - timedelta(days=30)
    queryset = Article.objects.published().annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5]
    template_name = "blog/article.html"
    context_object_name = "articles"
    paginate_by = 4

def detail(request, slug):

    context = {
        "article": get_object_or_404(Article, slug=slug, status="p"),
    }
    
    article = get_object_or_404(Article.objects.published(), slug=slug)
    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)

    return render(request, "blog/detail.html", context)

#class ArticleDetail(DetailView):
#    
#    def get_object(self):
#        slug = self.kwargs.get('slug')
#        article = get_object_or_404(Article.objects.published(), slug=slug)
#        ip_address = self.request.user.ip_address
#        if ip_address not in article.hits.all():
#           article.hits.add(ip_address)
#
#        return article

#class ArticlePreview(AuthorAccessMixin, DetailView):
#    
#    def get_object(self):
#        pk = self.kwargs.get('pk')
#        return get_object_or_404(Article, pk=pk)

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

#class CategoryList(ListView):
#    paginate_by = 4
#
#    def get_queryset(self):
#        global category
#        slug = self.kwargs.get('slug')
#        category = get_object_or_404(Category.objects.active(), slug=slug)
#        return category.articles.published()
#
#    def def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["category"] = category
#        return context

class AuthorList(ListView):
    paginate_by = 4
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
    
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