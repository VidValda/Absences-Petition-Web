from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class RegistroEstudiantes(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    ci = models.IntegerField(blank=True, null=True)

class RegistroPermisos(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    )

    materia = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    justificacion = models.FileField(upload_to='pdfs/', blank=True, null=True)
    project = models.ForeignKey(RegistroEstudiantes, on_delete=models.CASCADE,blank=True, null=True)
    id_solicitud = models.IntegerField(blank=True, null=True)
    horaFin = models.TimeField(blank=True, null=True)
    horaInicio = models.TimeField(blank=True, null=True)
    fechaSolicitud = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    descripcion = models.TextField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    

# class Petition(models.Model):
#     student_name = models.CharField(max_length=100)
#     petition_text = models.TextField()
#     status = models.CharField(max_length=10)
