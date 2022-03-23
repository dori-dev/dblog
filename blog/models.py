"""models of blog application
"""
import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
# from django.utils.translation import gettext as _  # TODO fa humanize date
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


def validate_file_extension(file_name: str) -> None:
    extension = os.path.splitext(file_name.name)[1]
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
    avatar = models.ImageField(
        default='files/user_avatar/avatar.png',
        upload_to='files/user_avatar/',
        null=True, blank=True,
        validators=[validate_file_extension],
    )
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    """articles of blog
    """
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(
        upload_to='files/article_cover/',
        null=False, blank=False,
        validators=[validate_file_extension],
    )
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def get_date(self):  # TODO fa humanize
        return humanize.naturaltime(self.created_at)

    def __str__(self):
        return self.title


class Category(models.Model):
    """category of blog articles"""
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(
        upload_to='files/category_cover/',
        null=False, blank=False,
        validators=[validate_file_extension],
    )

    def __str__(self):
        return self.title
