from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldMixin, FormValidMixin, AuthorAccessMixin
from django.views.generic import ListView, CreateView, UpdateView
from blogcore.models import Article, Category

#@login_required
#def home(request):
#    return render(request, 'registration/home.html')


class ArticleList(LoginRequiredMixin, ListView):
    #queryset = Article.objects.all()
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
    
class ArticleCreate(LoginRequiredMixin, FormValidMixin, FieldMixin, CreateView):
    model = Article
    template_name = "registration/article-create-update.html"

class ArticleUpdate(AuthorAccessMixin, FormValidMixin, FieldMixin, UpdateView):
    model = Article
    template_name = "registration/article-create-update.html"
