from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Blog(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='blogpost')
    img = models.ImageField(upload_to='pic', default='pix.jpeg', null=True, help_text='Recommended size 800x500 for '
                                                                                      'detail and 400x200 index')

    class Meta:
        verbose_name_plural = 'post'
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug, ])


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']
