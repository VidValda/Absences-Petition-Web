from django.core.management.base import BaseCommand
from fabio.models import RegistroPermisos, RegistroEstudiantes  # Import your models
from datetime import datetime

class Command(BaseCommand):
    help = 'Send dummy data to models'

    def handle(self, *args, **kwargs):
        # Dummy data for TodoItem
        

        # Dummy data for RegistroPermisos
        registro_permisos_data = [
            {
                "materia": "Mathematics",
                "fecha": datetime(2023, 9, 19).date(),
                "justificacion": None,
                "project_id": 1,
                "horaFin": "15:30:00",
                "horaInicio": "14:00:00",
                "fechaSolicitud": datetime(2023, 9, 15).date(),
                "estado": "pendiente",
                "descripcion": "Request for permission to attend a seminar.",
                "observacion": "",
            },
            {
                "materia": "Science",
                "fecha": datetime(2023, 9, 20).date(),
                "justificacion": None,
                "project_id": 2,
                "horaFin": "17:00:00",
                "horaInicio": "16:00:00",
                "fechaSolicitud": datetime(2023, 9, 16).date(),
                "estado": "pendiente",
                "descripcion": "Request for permission to conduct a lab experiment.",
                "observacion": "",
            },
        ]

        # Dummy data for RegistroEstudiantes
        registro_estudiantes_data = [
            {
                "name": "John",
                "apellido": "Doe",
                "email": "john.doe@example.com",
                "ci": 1234567,
            },
            {
                "name": "Jane",
                "apellido": "Smith",
                "email": "jane.smith@example.com",
                "ci": 9876543,
            },
            {
                "name": "Alice",
                "apellido": "Johnson",
                "email": "alice.johnson@example.com",
                "ci": 5432167,
            },
        ]


        # Create RegistroPermisos instances
        for permiso_data in registro_permisos_data:
            RegistroPermisos.objects.create(**permiso_data)

        # Create RegistroEstudiantes instances
        for estudiante_data in registro_estudiantes_data:
            RegistroEstudiantes.objects.create(**estudiante_data)

        self.stdout.write(self.style.SUCCESS('Dummy data sent successfully.'))
