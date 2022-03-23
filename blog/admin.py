"""blog admin
"""
from django.contrib import admin
from .models import UserProfile, Article, Category


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'description']

    def name(self, model: object):
        return f"{model.user.first_name} {model.user.last_name}"


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
