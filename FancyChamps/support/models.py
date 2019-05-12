from django.db import models

# Create your models here.

class SupportQueries(models.Model):
    user = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    mobile_no = models.IntegerField()
    question = models.CharField(max_length=255)
    brief_description = models.TextField()

    def __str__(self):
        return self.user + '/' + self.email
