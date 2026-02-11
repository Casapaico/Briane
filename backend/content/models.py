from django.db import models


class PageContent(models.Model):
    page_slug = models.CharField('Pagina', max_length=100, db_index=True)
    section_key = models.CharField('Seccion', max_length=100)
    title = models.CharField('Titulo', max_length=200, blank=True)
    content = models.TextField('Contenido', blank=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Contenido de pagina'
        verbose_name_plural = 'Contenidos de pagina'
        ordering = ['page_slug', 'order']
        unique_together = ['page_slug', 'section_key']

    def __str__(self):
        return f'{self.page_slug} - {self.section_key}'


class PageImage(models.Model):
    page_slug = models.CharField('Pagina', max_length=100, db_index=True)
    section_key = models.CharField('Seccion', max_length=100)
    image = models.ImageField('Imagen', upload_to='pages/')
    alt_text = models.CharField('Texto alternativo', max_length=200, blank=True)
    caption = models.CharField('Leyenda', max_length=300, blank=True)
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Imagen de pagina'
        verbose_name_plural = 'Imagenes de pagina'
        ordering = ['page_slug', 'order']

    def __str__(self):
        return f'{self.page_slug} - {self.section_key} ({self.order})'


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('equipo', 'Equipo'),
        ('eventos', 'Eventos'),
        ('comunidad', 'Comunidad'),
        ('academia', 'Academia'),
        ('proyectos', 'Proyectos'),
        ('oficina', 'Oficina'),
    ]

    category = models.CharField('Categoria', max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField('Imagen', upload_to='gallery/')
    title = models.CharField('Titulo', max_length=200, blank=True)
    description = models.TextField('Descripcion', blank=True)
    person_name = models.CharField('Nombre de persona', max_length=150, blank=True)
    person_comment = models.TextField('Comentario', blank=True)
    year = models.PositiveIntegerField('Ano', blank=True, null=True)
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Imagen de galeria'
        verbose_name_plural = 'Imagenes de galeria'
        ordering = ['category', 'order']

    def __str__(self):
        return self.title or f'{self.get_category_display()} ({self.order})'
