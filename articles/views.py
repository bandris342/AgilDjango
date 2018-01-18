from django.shortcuts import render
from .models import Articles

# Create your views here.

def articles_list(request):
    articles_list = Articles.objects.all().order_by('created_at')
    context = {'articles': articles_list}
    return render(request, 'articles/ListArticles.html', context)

def article_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/DetailArticle.html', context)