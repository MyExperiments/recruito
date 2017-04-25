from django.db import models
from django.contrib.auth.models import User
from .recruiter_models import Recruiter
from .base_models import AbstractBaseModel

class Job(AbstractBaseModel):
    """
    Job
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title
