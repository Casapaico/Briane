from rest_framework import serializers

from .models import (
    ContactSubmission, JobPosition,
    FullJobApplication, WorkExperience, AcademicFormation,
    NewsletterSubscription, ClaimBook,
)


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = [
            'name', 'email', 'phone', 'company', 'service',
            'other_service_detail', 'message', 'privacy_accepted',
        ]


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ['id', 'title', 'description']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['company', 'position', 'start_date', 'end_date']


class AcademicFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicFormation
        fields = ['subject', 'degree', 'graduation_date', 'university', 'grade']


class FullJobApplicationSerializer(serializers.ModelSerializer):
    work_experiences = WorkExperienceSerializer(many=True, required=False)
    academic_formations = AcademicFormationSerializer(many=True, required=False)

    class Meta:
        model = FullJobApplication
        fields = [
            'has_cv',
            # Contacto
            'title', 'first_name', 'last_name', 'email', 'phone',
            # Direccion
            'address', 'postal_code', 'city', 'state', 'country',
            # Idioma
            'preferred_language',
            # Archivos
            'cv_file', 'cover_letter', 'certificates', 'other_files',
            # Preguntas
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
            # Gestion
            'position',
            # Nested
            'work_experiences', 'academic_formations',
        ]

    def validate(self, data):
        if data.get('has_cv') and not self.initial_data.get('cv_file'):
            raise serializers.ValidationError(
                {'cv_file': 'Debe adjuntar su CV si selecciono "Cargar curriculum".'}
            )
        return data

    def create(self, validated_data):
        work_experiences_data = validated_data.pop('work_experiences', [])
        academic_formations_data = validated_data.pop('academic_formations', [])
        application = FullJobApplication.objects.create(**validated_data)
        for we_data in work_experiences_data:
            WorkExperience.objects.create(application=application, **we_data)
        for af_data in academic_formations_data:
            AcademicFormation.objects.create(application=application, **af_data)
        return application


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        extra_kwargs = {
            'email': {'validators': []},
        }

    def validate_email(self, value):
        if NewsletterSubscription.objects.filter(email=value, is_active=True).exists():
            raise serializers.ValidationError('Este correo ya esta suscrito al boletin.')
        return value

    def create(self, validated_data):
        sub, created = NewsletterSubscription.objects.update_or_create(
            email=validated_data['email'],
            defaults={'is_active': True},
        )
        return sub


class ClaimBookSerializer(serializers.ModelSerializer):
    """Serializer para el Libro de Reclamaciones"""

    class Meta:
        model = ClaimBook
        fields = [
            # Identificacion del consumidor
            'consumer_name',
            'consumer_document_type',
            'consumer_document_number',
            'consumer_address',
            'consumer_phone',
            'consumer_email',
            # Identificacion del bien contratado
            'service_type',
            'service_description',
            'service_date',
            'service_amount',
            'invoice_number',
            # Detalle de la reclamacion
            'complaint_type',
            'complaint_detail',
            'consumer_request',
        ]

    def validate_consumer_document_number(self, value):
        """Validar formato basico del numero de documento"""
        if not value or not value.strip():
            raise serializers.ValidationError('El numero de documento es requerido.')
        return value.strip()

    def validate_complaint_detail(self, value):
        """Validar que el detalle tenga contenido suficiente"""
        if len(value.strip()) < 20:
            raise serializers.ValidationError(
                'El detalle del reclamo debe tener al menos 20 caracteres.'
            )
        return value.strip()

    def validate_consumer_request(self, value):
        """Validar que el pedido tenga contenido suficiente"""
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                'El pedido debe tener al menos 10 caracteres.'
            )
        return value.strip()
