from django.db import models


class CompanyInfo(models.Model):
    name = models.CharField('Nombre', max_length=200, default='BRIANE')
    tagline = models.CharField('Eslogan', max_length=300, blank=True)
    description = models.TextField('Descripcion', blank=True)
    mission = models.TextField('Mision', blank=True)
    vision = models.TextField('Vision', blank=True)
    values = models.JSONField('Valores', default=list, blank=True)
    address = models.TextField('Direccion', blank=True)
    phones = models.JSONField('Telefonos', default=list, blank=True)
    emails = models.JSONField('Correos electronicos', default=list, blank=True)
    hours = models.CharField('Horario de atencion', max_length=200, blank=True)
    social_links = models.JSONField('Redes sociales', default=dict, blank=True)
    google_maps_embed_url = models.URLField('URL de Google Maps', max_length=500, blank=True)
    whatsapp_number = models.CharField('Numero de WhatsApp', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Informacion de la empresa'
        verbose_name_plural = 'Informacion de la empresa'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Stat(models.Model):
    value = models.CharField('Valor', max_length=50)
    label = models.CharField('Etiqueta', max_length=100)
    suffix = models.CharField('Sufijo', max_length=20, blank=True)
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Estadistica'
        verbose_name_plural = 'Estadisticas'
        ordering = ['order']

    def __str__(self):
        return f'{self.value} {self.label}'


class TeamMember(models.Model):
    name = models.CharField('Nombre', max_length=200)
    position = models.CharField('Cargo', max_length=200)
    bio = models.TextField('Biografia', blank=True)
    image = models.ImageField('Foto', upload_to='team/', blank=True)
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Miembro del equipo'
        verbose_name_plural = 'Miembros del equipo'
        ordering = ['order']

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Nombre', max_length=200)
    logo = models.ImageField('Logo', upload_to='clients/')
    url = models.URLField('Sitio web', blank=True)
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['order']

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField('Titulo', max_length=300)
    slug = models.SlugField('Slug', unique=True)
    excerpt = models.TextField('Extracto', blank=True)
    content = models.TextField('Contenido')
    date = models.DateField('Fecha')
    category = models.CharField('Categoria', max_length=100, blank=True)
    image = models.ImageField('Imagen', upload_to='news/', blank=True)
    is_published = models.BooleanField('Publicado', default=False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['-date']

    def __str__(self):
        return self.title
