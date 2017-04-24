from django.conf.urls import url;

from .views.job_views import *;

urlpatterns = [
    url(r'^jobs/$', jobs, name='index')
]