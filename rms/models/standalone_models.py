from django.db import models
from .base_models import AbstractBaseModel

class Skill(AbstractBaseModel):
    """
    Skill
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Designation(AbstractBaseModel):
    """
    Designation
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
