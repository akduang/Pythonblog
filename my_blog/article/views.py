from django.shortcuts import render

from django.http import HttpRequest

# Create your views here.

def article_list(request):
  return HttpRequest("Hello World")
