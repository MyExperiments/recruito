from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)