from django.contrib import admin

from .models import (
    ContactSubmission, JobPosition,
    FullJobApplication, WorkExperience, AcademicFormation,
    NewsletterSubscription,
)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'is_read', 'created_at']
    list_filter = ['is_read', 'service', 'created_at']
    search_fields = ['name', 'email', 'company', 'message']
    list_editable = ['is_read']
    readonly_fields = [
        'name', 'email', 'phone', 'company', 'service',
        'other_service_detail', 'message', 'privacy_accepted', 'created_at',
    ]
    fieldsets = [
        ('Datos del contacto', {
            'fields': ['name', 'email', 'phone', 'company'],
        }),
        ('Consulta', {
            'fields': ['service', 'other_service_detail', 'message', 'privacy_accepted'],
        }),
        ('Gestion interna', {
            'fields': ['is_read', 'notes', 'created_at'],
        }),
    ]

    def has_add_permission(self, request):
        return False


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['title']



class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 0
    readonly_fields = ['company', 'position', 'start_date', 'end_date']

    def has_add_permission(self, request, obj=None):
        return False


class AcademicFormationInline(admin.TabularInline):
    model = AcademicFormation
    extra = 0
    readonly_fields = ['subject', 'degree', 'graduation_date', 'university', 'grade']

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(FullJobApplication)
class FullJobApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name_display', 'email', 'position', 'is_reviewed', 'created_at']
    list_filter = ['is_reviewed', 'position', 'english_level', 'logistics_experience']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_editable = ['is_reviewed']
    inlines = [WorkExperienceInline, AcademicFormationInline]
    readonly_fields = [
        'has_cv',
        'title', 'first_name', 'last_name', 'email', 'phone',
        'address', 'postal_code', 'city', 'state', 'country',
        'preferred_language',
        'cv_file', 'cover_letter', 'certificates', 'other_files',
        'has_driver_license', 'driver_license_category',
        'has_criminal_record', 'criminal_record_detail',
        'has_health_issues', 'health_issues_detail',
        'available_immediately', 'available_travel', 'available_relocate',
        'has_own_vehicle',
        'english_level', 'excel_level', 'logistics_experience',
        'expected_salary', 'current_salary',
        'how_found', 'how_found_detail',
        'has_worked_here_before', 'worked_here_detail',
        'has_relatives_here', 'relatives_detail',
        'additional_info',
        'position', 'created_at',
    ]
    fieldsets = [
        ('Contacto', {
            'fields': [
                'title', 'first_name', 'last_name', 'email', 'phone',
                'preferred_language',
            ],
        }),
        ('Direccion', {
            'fields': ['address', 'postal_code', 'city', 'state', 'country'],
            'classes': ['collapse'],
        }),
        ('Archivos', {
            'fields': ['has_cv', 'cv_file', 'cover_letter', 'certificates', 'other_files'],
        }),
        ('Preguntas', {
            'fields': [
                'has_driver_license', 'driver_license_category',
                'has_criminal_record', 'criminal_record_detail',
                'has_health_issues', 'health_issues_detail',
                'available_immediately', 'available_travel', 'available_relocate',
                'has_own_vehicle',
                'english_level', 'excel_level', 'logistics_experience',
                'expected_salary', 'current_salary',
                'how_found', 'how_found_detail',
                'has_worked_here_before', 'worked_here_detail',
                'has_relatives_here', 'relatives_detail',
                'additional_info',
            ],
            'classes': ['collapse'],
        }),
        ('Gestion interna', {
            'fields': ['position', 'is_reviewed', 'notes', 'created_at'],
        }),
    ]

    @admin.display(description='Nombre completo')
    def full_name_display(self, obj):
        return obj.full_name

    def has_add_permission(self, request):
        return False


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['email']
    list_editable = ['is_active']

    def has_add_permission(self, request):
        return False
