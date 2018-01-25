from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Articles
from .forms import PostForm

# Create your views here.

def articles_list(request):
    articles_list = Articles.objects.all().order_by('created_at')
    context = {'articles': articles_list}
    return render(request, 'articles/ListArticles.html', context)

def article_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/DetailArticle.html', context)

def article_edit(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    form = PostForm(request.POST, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.updated_at = timezone.now()
        article.save()
    else:
        form = PostForm(instance=article)
    return render(request, 'articles/EditArticle.html', {'form': form})
