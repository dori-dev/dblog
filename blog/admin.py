"""blog admin
"""
from django.contrib import admin
from .models import UserProfile, Article, Category


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'category', 'author', 'date']
    list_filter = ['category', 'author', 'created_at']

    def date(self, model: object):
        return model.created_at.date()
    date.short_description = "Created At"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
