from django.shortcuts import render;

from rms.models.job_models import Job
from rms.utils.paginator import CustomPaginator

def jobs(request):
    page = request.GET.get('page')

    paginator = CustomPaginator()

    jobs = paginator.paginate(Job.objects.all(), page=page, per_page=25)

    return render(request, 'jobs/index.html', {'jobs': jobs});

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'jobs/show.html', {'job': job});
