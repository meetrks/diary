from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('tags/', views.TagList.as_view(), name='tags'),
    path('tags/<slug:slug>/', views.ArticleList.as_view(), name='tags'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
]
