from django.shortcuts import render
from django.views import View
from article_module.models import Article
from django.views.generic.list import ListView
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
    paginate_by = 5
    template_name  = 'article_module/articles_page.html'
