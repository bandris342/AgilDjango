from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='login')
def article_edit(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    form = PostForm(request.POST, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.updatedby = str(request.user)
        article.updated_at = timezone.now()
        article.save()
        message = "Article succesfully updated at " + article.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        context = {"message": message , "form": form}
    else:
        form = PostForm(instance=article)
        context = {"message": "", "form": form}
    return render(request, 'articles/EditArticle.html', context)

@login_required(login_url='login')
def article_new(request):
    form = PostForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = str(request.user)
        article.created_at = timezone.now()
        article.updated_at = article.created_at
        article.save()
        message = "Article succesfully saved at " + article.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        context = {"message": message , "form": form}
    else:
        form = PostForm()
        context = {"message": "", "form": form}
    return render(request, 'articles/EditArticle.html', context)

@login_required(login_url='login')
def article_delete(request, pk):
    article = Articles.objects.get(pk=pk)
    message = article.title + " succesfully deleted."
    article.delete()
    context = {"message": message}
    return render(request, 'articles/Message.html', context)