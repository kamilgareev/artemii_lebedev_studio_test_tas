from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import SpecialistsRegistry
from .serializers import SpecialistsRegistryViewSetSerializer


@extend_schema(tags=['Модель SpecialistsRegistry'])
@extend_schema_view(
    list=extend_schema(
        summary='Получение списка специалистов'
    ),
    retrieve=extend_schema(
        summary='Получение данных конкретного специалиста'
    ),
    update=extend_schema(
        summary='Изменение данных специалиста'
    ),
    partial_update=extend_schema(
        summary='Частичное изменение данных специалиста'
    ),
    create=extend_schema(
        summary='Создание записи о специалисте'
    ),
    destroy=extend_schema(
        summary='Удаление записи о специалисте'
    ),
)
class SpecialistsRegistryViewSet(ModelViewSet):
    queryset = SpecialistsRegistry.objects.all()
    serializer_class = SpecialistsRegistryViewSetSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'name', 'location', 'speciality', 'certification_category',
                        'category_assignment_order', 'contact_details']
    search_fields = ['id', 'name', 'location', 'speciality', 'certification_category',
                     'category_assignment_order', 'contact_details']
