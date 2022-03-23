"""blog views
"""
from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserProfile, Article, Category


class IndexPage(TemplateView):
    """index page view
    """

    def get(self, request: object, **kwargs):
        all_articles: List[object] = Article.objects.all()[:9]
        article_data: object = map(self.create_article_data, all_articles)
        context = {
            'article_data': list(article_data)
        }
        return render(request, 'index.html', context)

    @staticmethod
    def create_article_data(article: object) -> dict:
        """create data for articles with article object

        Args:
            article (object): object of article

        Returns:
            dict: article values
        """
        return {
            'title': article.title,
            'cover': article.cover.url,
            'category': article.category.title,
            'created_at': article.created_at,
        }
