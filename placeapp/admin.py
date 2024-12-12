from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import User, Student, Company, CompanyRecruiter, JobOpening, PlacementSession

# Register the User model with default UserAdmin
admin.site.register(User)

# Register other models
admin.site.register(Student)

admin.site.register(CompanyRecruiter)
admin.site.register(JobOpening)
admin.site.register(PlacementSession)




# admin.py
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'contact_email', 'website', 'company_picture']
    search_fields = ['name', 'location', 'contact_email']
    list_filter = ['location', 'website']
    ordering = ['name']  # Optional: to order companies alphabetically by name
    fields = ['name', 'description', 'location', 'contact_email', 'contact_phone', 'website', 'company_picture']  # Form fields order
from django.contrib import admin
from .models import JobApplication

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'shortlisted', 'contacted', 'applied_on')
    list_filter = ('shortlisted', 'contacted', 'education_level')
    search_fields = ('name', 'email', 'skills')

    # You can also add filters or search capabilities here
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'cover_letter', 'resume', 'shortlisted', 'contacted')
        }),
    )

admin.site.register(JobApplication, JobApplicationAdmin)
