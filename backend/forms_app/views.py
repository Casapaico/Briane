import json

from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import JobPosition
from .serializers import (
    ContactSubmissionSerializer, JobPositionSerializer,
    FullJobApplicationSerializer, NewsletterSubscriptionSerializer,
)


class ContactSubmissionCreateView(generics.CreateAPIView):
    serializer_class = ContactSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Mensaje enviado correctamente.'},
            status=status.HTTP_201_CREATED,
        )


class JobPositionListView(generics.ListAPIView):
    serializer_class = JobPositionSerializer
    pagination_class = None
    queryset = JobPosition.objects.filter(is_active=True)


class FullJobApplicationCreateView(generics.CreateAPIView):
    serializer_class = FullJobApplicationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # Parse nested JSON strings
        for field in ('work_experiences', 'academic_formations'):
            value = data.get(field)
            if isinstance(value, str):
                try:
                    data[field] = json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    data[field] = []
            elif value is None:
                data[field] = []

        # Convert boolean string fields
        bool_fields = [
            'has_cv', 'has_driver_license', 'has_criminal_record',
            'has_health_issues', 'available_immediately', 'available_travel',
            'available_relocate', 'has_own_vehicle', 'has_worked_here_before',
            'has_relatives_here',
        ]
        for field in bool_fields:
            value = data.get(field)
            if isinstance(value, str):
                data[field] = value.lower() in ('true', '1', 'yes')

        # Convert empty string salary fields to None
        for field in ('expected_salary', 'current_salary'):
            value = data.get(field)
            if value == '' or value is None:
                data[field] = None

        # Convert empty position to None
        if data.get('position') == '' or data.get('position') is None:
            data['position'] = None

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Postulacion enviada correctamente.'},
            status=status.HTTP_201_CREATED,
        )


class NewsletterSubscriptionCreateView(generics.CreateAPIView):
    serializer_class = NewsletterSubscriptionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Suscripcion realizada correctamente.'},
            status=status.HTTP_201_CREATED,
        )
