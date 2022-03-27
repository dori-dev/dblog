"""blog views
"""
from typing import List
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Category, UserProfile, User
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
        'promote': article.promote}


class IndexPage(TemplateView):
    """index page view
    """

    def get(self, request: HttpRequest):
        # all articles data
        all_articles: List[object] = Article.objects.all().order_by(
            "-created_at")[:12]
        article_data: List[dict] = list(
            map(get_article_data, all_articles))
        # all promote articles data
        all_promote_articles: List[object] = Article.objects.filter(
            promote=True)[:3]
        promote_data: List[dict] = list(
            map(get_article_data, all_promote_articles))
        # render page
        context: dict = {
            'article_data': article_data,
            'promote_article_data': promote_data}
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

    def get(self, request: HttpRequest):
        try:
            all_articles: List[object] = Article.objects.all().order_by(
                '-created_at')[:10]
            article_data: List[dict] = list(
                map(get_article_data, all_articles))
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(
                {'data': article_data},
                status=status.HTTP_200_OK)


class SingleArticleAPIView(APIView):
    def get(self, request: HttpRequest):
        try:
            article_title: str = request.GET['article_title']
            article: List[object] = Article.objects.filter(
                title__contains=article_title)
            serialized_data: list = serializers.SingleArticleSerializer(
                article, many=True)
            data: list = serialized_data.data
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(
                {'data': data},
                status=status.HTTP_200_OK)


class SearchArticleAPIView(APIView):
    def get(self, request: HttpRequest):
        try:
            query: str = request.GET['query']
            articles: List[object] = Article.objects.filter(
                Q(content__icontains=query))
            data: List[dict] = list(
                map(get_article_data, articles))
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(
                {'data': data},
                status=status.HTTP_200_OK)


class SubmitArticleAPIView(APIView):
    def post(self, request: HttpRequest):
        try:
            serializer = serializers.SubmitArticleSerializer(data=request.data)
            if serializer.is_valid():
                title = serializer.data.get('title')
                cover = request.FILES['cover']
                content = serializer.data.get('content')
                category_id = serializer.data.get('category_id')
                author_id = serializer.data.get('author_id')
                promote = serializer.data.get('promote')
            else:
                return Response(
                    {'status': 'Bad Request.'},
                    status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(id=author_id)
            author = UserProfile.objects.get(user=user)
            category = Category.objects.get(id=category_id)
            article = Article()
            article.title = title
            article.cover = cover
            article.content = content
            article.category = category
            article.author = author
            article.promote = promote
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            article.save()
            return Response(
                {'status': "OK"},
                status=status.HTTP_200_OK)


class UpdateArticleAPIView(APIView):
    def post(self, request: HttpRequest):
        try:
            serializer = serializers.UpdateArticleCoverSerializer(
                data=request.data)
            if serializer.is_valid():
                article_id = serializer.data.get('article_id')
                cover = request.FILES['cover']
            else:
                return Response(
                    {'status': 'Bad Request.'},
                    status=status.HTTP_400_BAD_REQUEST)
            article = Article.objects.get(id=article_id)
            article.cover = cover
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            article.save()
            return Response(
                {'status': "OK"},
                status=status.HTTP_200_OK)


class DeleteArticleAPIView(APIView):
    def post(self, request: HttpRequest):
        try:
            serializer = serializers.DeleteArticleSerializer(data=request.data)
            if serializer.is_valid():
                article_id = serializer.data.get('article_id')
            else:
                return Response(
                    {'status': 'Bad Request.'},
                    status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            message: str = "Internal Server Error, We'll Check It Later"
            return Response(
                {'status': message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            Article.objects.filter(id=article_id).delete()
            return Response(
                {'status': 'OK'},
                status=status.HTTP_200_OK)
