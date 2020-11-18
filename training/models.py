from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TrainingCourse(models.Model):

    # To recognize the fact that the admin may decide to create multiple articles
    #  (posts) without the intention of publishing, the individual may make and save drafts to be edited later

    TR_TYPE_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    STATUS_CHOICES = (
        ('ongoing', 'On going'),
        ('finished', 'Finished'),
    )

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    thumbnail = models.ImageField()

    title = models.CharField(max_length = 300)
    slug = models.SlugField(max_length=350,
                            unique_for_date='publish')

    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tr_type = models.CharField(max_length=20,
                              choices = TR_TYPE_CHOICES,
                              default = 'draft')
    status = models.CharField(max_length=50,
                              choices = STATUS_CHOICES,
                              default='ongoing')

    external_url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

    
