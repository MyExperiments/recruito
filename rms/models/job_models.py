from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import date
from .company_models import Company
from .standalone_models import Skill, Designation
from .base_models import AbstractBaseModel
from  ..constants import CURRENCIES

class Job(AbstractBaseModel):
    """
    Job
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_date = models.DateField()
    number_of_openings = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    keywords = models.CharField(max_length=150, blank=True)
    job_location = models.CharField(max_length=400, blank=True)
    min_year_of_experience = models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[MinValueValidator(0)])
    max_year_of_experience = models.DecimalField(default=0, max_digits=3, decimal_places=1, validators=[MinValueValidator(0)])
    min_salary = models.DecimalField(default=0, max_digits=30, decimal_places=5, validators=[MinValueValidator(0)])
    max_salary = models.DecimalField(default=0, max_digits=30, decimal_places=5, validators=[MinValueValidator(0)])
    salary_currency = models.CharField(max_length=10, choices=CURRENCIES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=False)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

    def is_expired(self):
        if date.today() > self.last_date:
            return True

