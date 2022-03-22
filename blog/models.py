"""models of blog application
"""
import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


def validate_file_extension(file_name: str):
    extension = os.path.splitext(file_name)[1]
    valid_extensions = [
        '.jpg',
        '.png',
        '.jpeg',
        '.gif'
    ]
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    """profile model for user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(
        default='files/user_avatar/avatar.png',
        upload_to='files/user_avatar/',
        null=True, blank=True,
        validators=[validate_file_extension],
    )
    description = models.CharField(max_length=512, null=False, blank=False)


class Article(models.Model):
    """article model
    """
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(
        upload_to='files/article_cover/',
        null=False, blank=False,
        validators=[validate_file_extension],
    )
    content = RichTextField()
    create_at = models.DateTimeField(default=datetime.now(), blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(
        upload_to='files/category_cover/',
        null=False, blank=False,
        validators=[validate_file_extension],
    )
