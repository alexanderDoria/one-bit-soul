from django.db import models
# Create your models here.


class Submission(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    date = models.DateField()
    subreddit = models.CharField(max_length=20)
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=100)
    upvotes = models.IntegerField()
    sentiment = models.FloatField()
