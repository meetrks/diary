from django.views import generic

from .models import Article, Tag


class ArticleList(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        is_approved_filter = {
            "is_approved": True
        }
        if self.request.user.is_authenticated and self.request.user.is_staff:
            is_approved_filter = {}
        queryset = Article.objects.filter(**is_approved_filter).order_by('-created')
        if self.kwargs.get("slug"):
            queryset = queryset.filter(tags__slug=self.kwargs.get("slug"))
        return queryset


class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'


class TagList(generic.ListView):
    queryset = Tag.objects.filter(is_approved=True)
    template_name = 'tag_list.html'
