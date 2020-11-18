from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):

    # To recognize the fact that the admin may decide to create multiple articles
    #  (posts) without the intention of publishing, the individual may make and save drafts to be edited later

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="blog_post")
    title = models.CharField(max_length = 300)
    slug = models.SlugField(max_length=350,
                            unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,
                              choices = STATUS_CHOICES,
                              default = 'draft')

    def __str__(self):
        return self.title

    
