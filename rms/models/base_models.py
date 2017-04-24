from django.db import models
from django.conf import settings


class AbstractBaseModel(models.Model):
    """
    Abstract base class model which should be used for subclassing other models
    """
    class Meta:
        abstract = True
        app_label = settings.RECRUITO_APPS['rms']

    def __unicode__(self):
        return self.name
