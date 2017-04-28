"""
All admin pages for models is included here
"""

from django.contrib import admin
from rms.models import *

class IndustryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'user')

class CompanyAdmin(admin.ModelAdmin):
    def edit_link(self, obj):
        return u'<a href="/admin/rms/company/%s/change/">Edit</a>' % (obj.id)

    edit_link.allow_tags = True
    edit_link.short_description = 'Actions'

    list_display = (
        'name', 'address', 'city', 'state', 'country', 'zipcode',
        'phone_number', 'edit_link'
    )

class CompanyUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company', 'user'
    )

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'last_date', 'created_by', 'company')

admin.site.register(IndustryType, IndustryTypeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Job, JobAdmin)