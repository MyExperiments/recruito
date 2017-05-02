from django.conf.urls import url;

from .views.job_views import *;

urlpatterns = [
    url(r'^jobs/$', jobs, name='all_jobs'),
    url(r'^jobs/(?P<job_id>\d+)/$', job_detail, name='job_detail')
]