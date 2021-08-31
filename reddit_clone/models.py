from django.core.exceptions import MiddlewareNotUsed
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.
class Subreddit(models.Model):
    thread = models.CharField(max_length=500)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-date_posted']

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
