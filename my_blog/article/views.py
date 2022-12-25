from django.shortcuts import render

# from django.http import HttpRequest

# Create your views here.

# def article_list(request):
#   return HttpRequest("Hello World")

from .models import ArticlePost

import markdown

def article_list(request):
  #取出所有博客文章
  articles = ArticlePost.objects.all()
  #传递给模板的对象
  context = { 'articles': articles }
  #render函数：载入模板，并返回context对象
  return render(request, 'article/list.html', context)

#文章详情
def article_detail(request, id):
  #取出相应的文章
  article = ArticlePost.objects.get(id=id)
  
  #渲染html
  article.body = markdown.markdown(article.body,
    extensions=[
      # 'markdown.extensions.extra',
      # 'markdown.extensions.codehilite',
    ]
  )
  #需要传递给模板的对象
  context = { 'article': article}
  #载入模板，并返回context对象
  return render(request, 'article/detail.html', context)