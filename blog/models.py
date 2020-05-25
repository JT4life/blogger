from django.db import models
from django.forms import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class Post(models.Model):
    status_choices = {('Draft','Draft'),('Published','Published')}
    title = models.CharField(max_length=100, default='', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True, blank=True)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete="", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=10, choices=status_choices, default='Draft')
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        if self.title == None:
            return "ERROR TITLE IS NULL"
        return self.title

class AddComment(models.Model):
    text = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=20, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='blog_comment', null=True)

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now,null=True, blank=True)
    approved_comment = models.BooleanField(default=False,null=True, blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comment.objects.filter_by_instance(instance)
    #     return qs
    #
    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type
'''
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)'''