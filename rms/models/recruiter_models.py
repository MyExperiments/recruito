from django.db import models
from .base_models import AbstractBaseModel

class RecruiterSector(AbstractBaseModel):
    """
    RecruiterSector
    """
    name = models.CharField('Sector', max_length=50)

    def __str__(self):
        return self.name

class Recruiter(AbstractBaseModel):
    """
    RecruiterSector
    """
    company = models.CharField('Company', max_length=50)
    sector = models.ForeignKey(RecruiterSector, on_delete=models.CASCADE)

    def __str__(self):
        return self.company
