from django.db import models

# Create your models here.


class Submission(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=300)
    url = models.CharField(max_length=100)
    upvotes = models.IntegerField()
    sentiment = models.IntegerField()


# class Metrics(models.Model):
#    id = models.CharField(max_length=10, primary_key=True)
#    date = models.DateField()
#    metric_type = models.CharField(max_length=10)
#    value = models.FloatField()
