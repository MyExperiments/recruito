"""
All admin pages for models is included here
"""

from django.contrib import admin
from rms.models import *

class IndustryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'user')

class RecruiterAdmin(admin.ModelAdmin):
    def edit_link(self, obj):
        return u'<a href="/admin/rms/recruiter/%s/change/">Edit</a>' % (obj.id)

    edit_link.allow_tags = True
    edit_link.short_description = "Actions"

    list_display = (
        'name', 'address', 'city', 'state', 'country', 'zipcode',
        'phone_number', 'edit_link'
    )

class RecruiterUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'recruiter', 'user'
    )

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'last_date', 'user', 'recruiter')

admin.site.register(IndustryType, IndustryTypeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(RecruiterUser, RecruiterUserAdmin)
admin.site.register(Job, JobAdmin)