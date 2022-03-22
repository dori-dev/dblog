"""blog admin
"""
from django.contrib import admin
from .models import UserProfile, Article, Category

admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Category)
