from django.db import models


class ContactSubmission(models.Model):
    SERVICE_CHOICES = [
        ('seguridad-electronica', 'Seguridad Electronica'),
        ('seguridad-fisica', 'Seguridad Fisica'),
        ('limpieza', 'Limpieza y Mantenimiento'),
        ('saneamiento', 'Saneamiento Ambiental'),
        ('consultoria', 'Consultoria'),
        ('otro', 'Otro'),
    ]

    name = models.CharField('Nombre', max_length=200)
    email = models.EmailField('Correo electronico')
    phone = models.CharField('Telefono', max_length=20, blank=True)
    company = models.CharField('Empresa', max_length=200, blank=True)
    service = models.CharField('Servicio', max_length=100, choices=SERVICE_CHOICES, blank=True)
    other_service_detail = models.CharField('Detalle otro servicio', max_length=200, blank=True)
    message = models.TextField('Mensaje')
    privacy_accepted = models.BooleanField('Acepto politica de privacidad', default=False)
    is_read = models.BooleanField('Leido', default=False)
    notes = models.TextField('Notas internas', blank=True)
    created_at = models.DateTimeField('Fecha de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.created_at:%d/%m/%Y %H:%M}'


class JobPosition(models.Model):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion', blank=True)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Puesto laboral'
        verbose_name_plural = 'Puestos laborales'
        ordering = ['order']

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    name = models.CharField('Nombre', max_length=200)
    email = models.EmailField('Correo electronico')
    phone = models.CharField('Telefono', max_length=20, blank=True)
    city = models.CharField('Ciudad', max_length=100, blank=True)
    position = models.ForeignKey(
        JobPosition,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Puesto',
    )
    cv_file = models.FileField('CV', upload_to='cvs/')
    is_reviewed = models.BooleanField('Revisado', default=False)
    notes = models.TextField('Notas internas', blank=True)
    created_at = models.DateTimeField('Fecha de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Postulacion laboral'
        verbose_name_plural = 'Postulaciones laborales'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.created_at:%d/%m/%Y %H:%M}'


class FullJobApplication(models.Model):
    TITLE_CHOICES = [
        ('Sr', 'Sr.'),
        ('Sra', 'Sra.'),
        ('Srta', 'Srta.'),
    ]
    LANGUAGE_CHOICES = [
        ('es', 'Espanol'),
        ('en', 'Ingles'),
        ('pt', 'Portugues'),
    ]
    ENGLISH_LEVEL_CHOICES = [
        ('none', 'Ninguno'),
        ('basic', 'Basico'),
        ('intermediate', 'Intermedio'),
        ('advanced', 'Avanzado'),
        ('native', 'Nativo'),
    ]
    EXCEL_LEVEL_CHOICES = [
        ('none', 'Ninguno'),
        ('basic', 'Basico'),
        ('intermediate', 'Intermedio'),
        ('advanced', 'Avanzado'),
    ]
    LOGISTICS_EXP_CHOICES = [
        ('none', 'Ninguna'),
        ('less_1', 'Menos de 1 ano'),
        ('1_3', '1 a 3 anos'),
        ('3_5', '3 a 5 anos'),
        ('more_5', 'Mas de 5 anos'),
    ]
    HOW_FOUND_CHOICES = [
        ('web', 'Pagina web'),
        ('social', 'Redes sociales'),
        ('referral', 'Referido'),
        ('job_portal', 'Portal de empleo'),
        ('other', 'Otro'),
    ]

    # Tab 1
    has_cv = models.BooleanField('Tiene CV', default=False)

    # Tab 2 - Contacto
    title = models.CharField('Titulo', max_length=10, choices=TITLE_CHOICES, blank=True)
    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    email = models.EmailField('Correo electronico')
    phone = models.CharField('Telefono', max_length=20)

    # Tab 2 - Direccion
    address = models.CharField('Direccion', max_length=300, blank=True)
    postal_code = models.CharField('Codigo postal', max_length=20, blank=True)
    city = models.CharField('Ciudad', max_length=100, blank=True)
    state = models.CharField('Departamento/Estado', max_length=100, blank=True)
    country = models.CharField('Pais', max_length=100, blank=True)

    # Tab 2 - Idioma
    preferred_language = models.CharField(
        'Idioma preferido', max_length=5, choices=LANGUAGE_CHOICES, default='es'
    )

    # Tab 2 - Archivos
    cv_file = models.FileField('Curriculum Vitae', upload_to='aplicar/cv/', blank=True)
    cover_letter = models.FileField('Carta de presentacion', upload_to='aplicar/cover/', blank=True)
    certificates = models.FileField('Certificados', upload_to='aplicar/certificates/', blank=True)
    other_files = models.FileField('Otros archivos', upload_to='aplicar/other/', blank=True)

    # Tab 3 - Preguntas
    has_driver_license = models.BooleanField('Tiene licencia de conducir', default=False)
    driver_license_category = models.CharField(
        'Categoria de licencia', max_length=20, blank=True
    )
    has_criminal_record = models.BooleanField('Tiene antecedentes penales', default=False)
    criminal_record_detail = models.CharField(
        'Detalle antecedentes', max_length=300, blank=True
    )
    has_health_issues = models.BooleanField('Tiene problemas de salud', default=False)
    health_issues_detail = models.CharField(
        'Detalle problemas de salud', max_length=300, blank=True
    )
    available_immediately = models.BooleanField('Disponibilidad inmediata', default=False)
    available_travel = models.BooleanField('Disponible para viajar', default=False)
    available_relocate = models.BooleanField('Disponible para reubicacion', default=False)
    has_own_vehicle = models.BooleanField('Tiene vehiculo propio', default=False)
    english_level = models.CharField(
        'Nivel de ingles', max_length=20, choices=ENGLISH_LEVEL_CHOICES, default='none'
    )
    excel_level = models.CharField(
        'Nivel de Excel', max_length=20, choices=EXCEL_LEVEL_CHOICES, default='none'
    )
    logistics_experience = models.CharField(
        'Experiencia en logistica', max_length=20, choices=LOGISTICS_EXP_CHOICES, default='none'
    )
    expected_salary = models.PositiveIntegerField('Salario esperado (S/.)', null=True, blank=True)
    current_salary = models.PositiveIntegerField('Salario actual (S/.)', null=True, blank=True)
    how_found = models.CharField(
        'Como se entero', max_length=20, choices=HOW_FOUND_CHOICES, blank=True
    )
    how_found_detail = models.CharField(
        'Detalle como se entero', max_length=200, blank=True
    )
    has_worked_here_before = models.BooleanField('Ha trabajado aqui antes', default=False)
    worked_here_detail = models.CharField(
        'Detalle trabajo previo', max_length=300, blank=True
    )
    has_relatives_here = models.BooleanField('Tiene familiares en la empresa', default=False)
    relatives_detail = models.CharField(
        'Detalle familiares', max_length=300, blank=True
    )
    additional_info = models.TextField('Informacion adicional', blank=True)

    # Gestion
    position = models.ForeignKey(
        JobPosition,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Puesto',
        related_name='full_applications',
    )
    is_reviewed = models.BooleanField('Revisado', default=False)
    notes = models.TextField('Notas internas', blank=True)
    created_at = models.DateTimeField('Fecha de envio', auto_now_add=True)

    class Meta:
        verbose_name = 'Postulacion completa'
        verbose_name_plural = 'Postulaciones completas'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.created_at:%d/%m/%Y %H:%M}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class WorkExperience(models.Model):
    application = models.ForeignKey(
        FullJobApplication,
        on_delete=models.CASCADE,
        related_name='work_experiences',
        verbose_name='Postulacion',
    )
    company = models.CharField('Empresa', max_length=200)
    position = models.CharField('Puesto', max_length=200)
    start_date = models.DateField('Fecha de inicio', null=True, blank=True)
    end_date = models.DateField('Fecha de fin', null=True, blank=True)

    class Meta:
        verbose_name = 'Experiencia laboral'
        verbose_name_plural = 'Experiencias laborales'
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.company} - {self.position}'


class AcademicFormation(models.Model):
    DEGREE_CHOICES = [
        ('secondary', 'Secundaria'),
        ('technical', 'Tecnico'),
        ('bachelor', 'Bachiller'),
        ('licentiate', 'Licenciatura'),
        ('master', 'Maestria'),
        ('doctorate', 'Doctorado'),
        ('other', 'Otro'),
    ]

    application = models.ForeignKey(
        FullJobApplication,
        on_delete=models.CASCADE,
        related_name='academic_formations',
        verbose_name='Postulacion',
    )
    subject = models.CharField('Especialidad', max_length=200)
    degree = models.CharField('Grado', max_length=20, choices=DEGREE_CHOICES, blank=True)
    graduation_date = models.DateField('Fecha de graduacion', null=True, blank=True)
    university = models.CharField('Universidad/Instituto', max_length=200, blank=True)
    grade = models.CharField('Nota/Promedio', max_length=20, blank=True)

    class Meta:
        verbose_name = 'Formacion academica'
        verbose_name_plural = 'Formaciones academicas'
        ordering = ['-graduation_date']

    def __str__(self):
        return f'{self.subject} - {self.university}'
