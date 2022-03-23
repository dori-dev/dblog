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
        # all articles data
        all_articles: List[object] = Article.objects.all().order_by(
            "-created_at"
        )[:12]
        article_data: List[dict] = list(
            map(self.get_article_data, all_articles)
        )
        # all promote articles data
        all_promote_articles: List[object] = Article.objects.filter(
            promote=True
        )[:5]
        promote_data: List[dict] = list(
            map(self.get_promote_article_data, all_promote_articles)
        )
        # render page
        context: dict = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }
        return render(request, 'index.html', context)

    @staticmethod
    def get_article_data(article: object) -> dict:
        """create data for articles with article object

        Args:
            article (object): object of article

        Returns:
            dict: article values
        """
        return {
            'category': article.category.title,
            'title': article.title,
            'cover': article.cover.url,
            'created_at': article.get_date,
        }

    def get_promote_article_data(self, promote_article: object) -> dict:
        """create data for promote articles with promote_article object

        Args:
            promote_article (object): object of promote article

        Returns:
            dict: promote article values
        """
        article_data = self.get_article_data(promote_article)
        article_data.update({
            'author': f"{promote_article.author.user.first_name} "
            f"{promote_article.author.user.last_name}",
            'avatar': promote_article.author.avatar.url,
        })
        return article_data
