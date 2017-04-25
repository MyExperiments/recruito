"""
All admin pages for models is included here
"""

from django.contrib import admin
from rms.models import *

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'role', 'user')

class RecruiterSectorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class RecruiterAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'sector')

class JobAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'description', 'last_date', 'user', 'recruiter')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(RecruiterSector, RecruiterSectorAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(Job, JobAdmin)