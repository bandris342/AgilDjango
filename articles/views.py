from django.shortcuts import render
from .models import Articles
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def articles_list(request):
    articles_list = Articles.objects.all().order_by('created_at')
    context = {'articles': articles_list}
    return render(request, 'articles/ListArticles.html', context)

def article_detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {'articles': article}
    return render(request, 'articles/DetailArticle.html', context)
def post_new(request):
      form = PostForm()
      article = form.save(commit=False)
      article.author = request.user
      article.save()
      return render(request, 'articles/create_article.html', {'form': form})
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.author = request.user
#             article.save()
#             return redirect('articles_list', pk=article.pk)
#     else:
#         form = PostForm()
#     return render(request, 'articles/create_article.html', {'form': form})   