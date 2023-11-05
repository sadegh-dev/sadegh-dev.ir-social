from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    '''
    Category class model in blog app

    name field is not primaryKey.
    '''
    name =     models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('posts:post_categories', args=[self.id])


class Post(models.Model):
    '''
    The Post Model Class

    User and Category are ForeignKey
    '''
    user =      models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    category =  models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='cposts')
    body =      models.TextField(max_length=500)
    created =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[self.created.year, self.created.month, self.created.day, self.id])


class Comment(models.Model):
    user =      models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ucomments')
    post =      models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomments')
    reply =     models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', null=True, blank=True)
    is_reply =  models.BooleanField(default=False)
    body =      models.TextField(max_length=400)
    created =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.full_name} - {self.body[:20]}'
    



