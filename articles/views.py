from django.views import generic

from .models import Article, Tag


class ArticleList(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Article.objects.filter(is_approved=True).order_by('-created')
        if self.kwargs.get("slug"):
            queryset = queryset.filter(tags__slug=self.kwargs.get("slug"))
        return queryset


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'


class TagList(generic.ListView):
    queryset = Tag.objects.filter(is_approved=True)
    template_name = 'tag_list.html'
