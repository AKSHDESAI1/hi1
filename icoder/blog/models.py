from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
import datetime
# Create your models here.
# Database ------> Excel Workspace
# Models In Django -------> Table ------> Sheet

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=25)
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    image2 = models.ImageField(upload_to='aksh1/')

    def __str__(self):
        return self.title + ' By ' + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment1 = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # timestamp = models.DateField(auto_now=True)
    # timestamp = datetime.datetime.now()
    # timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment1

