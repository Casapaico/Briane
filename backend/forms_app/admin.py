from django.contrib import admin

from .models import (
    ContactSubmission, JobPosition,
    FullJobApplication,
    NewsletterSubscription, ClaimBook,
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



@admin.register(FullJobApplication)
class FullJobApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name_display', 'email', 'position', 'is_reviewed', 'created_at']
    list_filter = ['is_reviewed', 'position', 'english_level', 'logistics_experience']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_editable = ['is_reviewed']
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


@admin.register(ClaimBook)
class ClaimBookAdmin(admin.ModelAdmin):
    list_display = [
        'claim_number', 'consumer_name', 'complaint_type',
        'status', 'created_at', 'response_date'
    ]
    list_filter = [
        'complaint_type', 'status', 'service_type',
        'consumer_document_type', 'created_at'
    ]
    search_fields = [
        'claim_number', 'consumer_name', 'consumer_document_number',
        'consumer_email', 'complaint_detail'
    ]
    list_editable = ['status']
    date_hierarchy = 'created_at'

    readonly_fields = [
        'claim_number',
        # Datos del consumidor
        'consumer_name', 'consumer_document_type', 'consumer_document_number',
        'consumer_address', 'consumer_phone', 'consumer_email',
        # Datos del servicio
        'service_type', 'service_description', 'service_date',
        'service_amount', 'invoice_number',
        # Detalle del reclamo
        'complaint_type', 'complaint_detail', 'consumer_request',
        # Metadata
        'created_at', 'updated_at', 'ip_address',
    ]

    fieldsets = [
        ('Numero de Reclamo', {
            'fields': ['claim_number', 'created_at'],
            'classes': ['wide'],
        }),
        ('Identificacion del Consumidor', {
            'fields': [
                'consumer_name',
                ('consumer_document_type', 'consumer_document_number'),
                'consumer_address',
                ('consumer_phone', 'consumer_email'),
            ],
        }),
        ('Identificacion del Bien Contratado', {
            'fields': [
                'service_type',
                'service_description',
                ('service_date', 'service_amount'),
                'invoice_number',
            ],
        }),
        ('Detalle de la Reclamacion', {
            'fields': [
                'complaint_type',
                'complaint_detail',
                'consumer_request',
            ],
        }),
        ('Gestion Interna', {
            'fields': [
                'status',
                'assigned_to',
                'internal_notes',
                'response',
                'response_date',
            ],
            'classes': ['wide'],
        }),
        ('Metadata', {
            'fields': ['ip_address', 'updated_at'],
            'classes': ['collapse'],
        }),
    ]

    def has_add_permission(self, request):
        """No permitir crear reclamos desde el admin, solo desde el formulario web"""
        return False

    def has_delete_permission(self, request, obj=None):
        """No permitir eliminar reclamos por requisitos legales"""
        return False

    def save_model(self, request, obj, form, change):
        """Auto-actualizar fecha de respuesta cuando se agrega una respuesta"""
        if obj.response and not obj.response_date:
            from django.utils import timezone
            obj.response_date = timezone.now()
        super().save_model(request, obj, form, change)
