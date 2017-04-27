from django.db import models
from django.contrib.auth.models import User
from .base_models import AbstractBaseModel

class IndustryType(AbstractBaseModel):
    """
    IndustryType
    """
    name = models.CharField('Industry Type', max_length=100)

    def __str__(self):
        return self.name

class Recruiter(AbstractBaseModel):
    """
    Recruiter
    """
    name = models.CharField('Name', max_length=100)
    address = models.CharField('Address', max_length=200)
    country = models.CharField('Country', max_length=100)
    city = models.CharField('District', max_length=100)
    state = models.CharField('State', max_length=100)
    zipcode = models.CharField('Pincode / Zipcode', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=30)
    industry_type = models.ManyToManyField(IndustryType)

    def __str__(self):
        return self.name

class RecruiterUser(AbstractBaseModel):
    """
    RecruiterUser
    """
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.recruiter.name + "-" + self.user.username
