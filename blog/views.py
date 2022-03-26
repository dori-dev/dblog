"""blog views
"""
from typing import List, Union
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from . import serializers


def get_article_data(article: object) -> dict:
    """create data for articles with article object

        Args:
            article (object): object of article

        Returns:
            dict: article values
        """
    return {
        'title': article.title,
        'category': article.category.title,
        'author': f"{article.author.user.first_name} "
        f"{article.author.user.last_name}",
        'created_at': article.get_date(),
        'avatar': article.author.avatar.url,
        'cover': article.cover.url,
        'content': article.content,
        'promote': article.promote,
    }


class IndexPage(TemplateView):
    """index page view
    """

    def get(self, request: object, **kwargs):
        # all articles data
        all_articles: List[object] = Article.objects.all().order_by(
            "-created_at"
        )[:12]
        article_data: List[dict] = list(
            map(get_article_data, all_articles)
        )
        # all promote articles data
        all_promote_articles: List[object] = Article.objects.filter(
            promote=True
        )[:3]
        promote_data: List[dict] = list(
            map(get_article_data, all_promote_articles)
        )
        # render page
        context: dict = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }
        return render(request, 'index.html', context)


class ContactPage(TemplateView):  # TODO dynamic data
    """contact-us page view
    """
    template_name = "page-contact.html"


class AboutPage(TemplateView):  # TODO dynamic data
    """about-me page view
    """
    template_name = "page-about.html"


class AllArticleAPIView(APIView):
    """all article api view"""

    def get(self, request, format=None):
        try:
            all_articles: List[object] = Article.objects.all().order_by(
                '-created_at'
            )[:10]
            article_data: List[dict] = list(
                map(get_article_data, all_articles)
            )
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            return Response(
                {'data': article_data},
                status=status.HTTP_200_OK
            )


class SingleArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            article_title: str = request.GET['article_title']
            article: Union[object, List[object]] = Article.objects.filter(
                title__contains=article_title
            )
            serialized_data: list = serializers.SingleArticleSerializer(
                article, many=True
            )
            data: list = serialized_data.data
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            return Response(
                {'data': data},
                status=status.HTTP_200_OK
            )
