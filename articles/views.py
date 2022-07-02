from django.views import generic

from .models import Article


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(is_approved=True).order_by('-created')
    template_name = 'index.html'


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'post_detail.html'
