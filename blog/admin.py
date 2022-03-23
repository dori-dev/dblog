"""blog admin
"""
from django.contrib import admin
from .models import UserProfile, Article, Category


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category', 'author', 'create_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
