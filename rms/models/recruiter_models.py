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
    company = models.CharField('Company', max_length=100)
    address = models.CharField('Address', max_length=200)
    country = models.CharField('Country', max_length=100)
    city = models.CharField('District', max_length=100)
    state = models.CharField('State', max_length=100)
    zipcode = models.CharField('Pincode / Zipcode', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=30)
    industry_type = models.ForeignKey(IndustryType, on_delete=models.CASCADE, null=False)
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.company

class RecruiterUser(AbstractBaseModel):
    """
    RecruiterUser
    """
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.company + "-" + self.user

class Experience(AbstractBaseModel):
    """
    Experience
    """
    name = models.CharField('Department', max_length=100)
    is_default = models.BooleanField('Is Default', default=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Designation(AbstractBaseModel):
    """
    Designation
    """
    name = models.CharField('Designation', max_length=100)
    is_default = models.BooleanField('Is Default', default=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Skill(AbstractBaseModel):
    """
    Skill
    """
    name = models.CharField('Skill', max_length=100)
    is_default = models.BooleanField('Is Default', default=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Department(AbstractBaseModel):
    """
    Department
    """
    name = models.CharField('Department', max_length=100)
    designations = models.ManyToManyField(Designation)
    is_default = models.BooleanField('Is Default', default=False)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
