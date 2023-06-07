from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views import View
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali
from article_module.models import Article, ArticleCategory, ArticleComment

# Create your views here.

# class ArticlesView(View):
#     def get(self, request):
#         article = Article.object.filter(is_active=True)    
#         context = {
#             'articles': article
#         }
#         return render(request, 'article_module/articles_page.html', context)
class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/articles_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        #context['comments'] = ArticleComment.objects
        #print(kwargs)
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent=None).prefetch_related('articlecomment_set')
        return context


def article_categories_component(request: HttpRequest):
    article_main_categories = ArticleCategory.objects.filter(is_active=True, parent_id=None)

    context = {
        'main_categories': article_main_categories
    }
    return render(request, 'article_module/components/article_categories_component.html', context)

def add_article_comment(request: HttpRequest):
    print(request.GET)
    return HttpResponse('response')
