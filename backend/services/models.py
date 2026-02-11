from django.db import models


class Service(models.Model):
    name = models.CharField('Nombre', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    short_description = models.CharField('Descripcion corta', max_length=300, blank=True)
    description = models.TextField('Descripcion', blank=True)
    features = models.JSONField('Caracteristicas', default=list, blank=True)
    image = models.ImageField('Imagen', upload_to='services/', blank=True)
    icon = models.CharField('Icono', max_length=100, blank=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['order']

    def __str__(self):
        return self.name
