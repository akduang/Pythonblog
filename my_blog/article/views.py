from django.shortcuts import render

# from django.http import HttpRequest

# Create your views here.

# def article_list(request):
#   return HttpRequest("Hello World")

from .models import ArticlePost

def article_list(request):
  #取出所有博客文章
  articles = ArticlePost.objects.all()
  #传递给模板的对象
  context = { 'articles': articles }
  #render函数：载入模板，并返回context对象
  return render(request, 'article/list.html', context)