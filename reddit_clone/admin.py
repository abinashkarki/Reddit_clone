from django.contrib import admin
from . models import Subreddit, Vote
# Register your models here.
admin.site.register(Subreddit)
admin.site.register(Vote)