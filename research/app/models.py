from django.db import models

# Create your models here.
class Publication(models.Model):
    first_author_name = models.CharField(max_length=50)
    second_author_name = models.CharField(max_length=50)
    third_author_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200,default="")
    journal = models.CharField(max_length=50)
    year_of_publication = models.IntegerField(default=2017)
    volume = models.IntegerField(default=1)
    issue = models.IntegerField(default=1)
    pp = models.CharField(max_length=15)
