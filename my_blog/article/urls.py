from django.urls import path
#引入views.py
from . import views
app_name = 'article'

urlpatterns = [
    #path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
]
