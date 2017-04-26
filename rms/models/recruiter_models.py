from django.db import models
from django.contrib.auth.models import User
from .base_models import AbstractBaseModel

class Recruiter(AbstractBaseModel):
    """
    Recruiter
    """
    company = models.CharField('Company', max_length=100)
    address = models.CharField('Address', max_length=200)
    country = models.CharField('Country', max_length=100)
    city = models.CharField('District', max_length=100)
    state = models.CharField('State', max_length=100)
    zipcode = models.CharField('Pincode / Zipcode', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=30)

    def __str__(self):
        return self.company

class RecruiterUser(AbstractBaseModel):
    """
    Recruiter
    """
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.company + "-" + self.user

