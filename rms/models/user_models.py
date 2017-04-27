"""
All User related models goes here.
"""
from django.db import models
from django.contrib.auth.models import User
from .base_models import AbstractBaseModel

class UserProfile(AbstractBaseModel):
    ROLES = (
        ('recruiter', 'Recruiter'),
        ('candidate', 'Candidate')
    )
    role = models.CharField('Role', choices=ROLES, max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
