from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class RegistroEstudiantes(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    ci = models.IntegerField()

class RegistroPermisos(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    )

    materia = models.TextField()
    fecha = models.DateField()
    justificacion = models.FileField(upload_to='pdfs/', blank=True, null=True)
    project = models.ForeignKey(RegistroEstudiantes, on_delete=models.CASCADE)

    horaFin = models.TimeField()
    horaInicio = models.TimeField()
    fechaSolicitud = models.DateField()
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    descripcion = models.TextField()
    observacion = models.TextField(blank=True, null=True)

    

# class Petition(models.Model):
#     student_name = models.CharField(max_length=100)
#     petition_text = models.TextField()
#     status = models.CharField(max_length=10)
