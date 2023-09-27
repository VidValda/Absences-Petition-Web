# myapp/management/commands/generate_dummy_data.py
import random
from django.core.management.base import BaseCommand
from fabio.models import RegistroEstudiantes, RegistroPermisos
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for RegistroEstudiantes and RegistroPermisos models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Generating dummy data...'))

        # Generate dummy data for RegistroEstudiantes
        for _ in range(10):
            RegistroEstudiantes.objects.create(
                name=fake.first_name(),
                apellido=fake.last_name(),
                email=fake.email(),
                ci=random.randint(1000000, 9999999),
            )

        # Generate dummy data for RegistroPermisos
        for _ in range(20):
            RegistroPermisos.objects.create(
                materia=fake.sentence(),
                fecha=fake.date_between(start_date='-30d', end_date='today'),
                justificacion=None,  # You can customize this field as needed
                project_id=random.randint(1, 10),  # Assuming there are 10 RegistroEstudiantes objects
                id_solicitud=random.randint(1, 100),
                horaFin=fake.time_object(end_datetime=None),
                horaInicio=fake.time_object(end_datetime=None),
                fechaSolicitud=fake.date_between(start_date='-90d', end_date='today'),
                estado=random.choice(['pendiente', 'aceptado', 'rechazado']),
                descripcion=fake.paragraph(),
                observacion=fake.paragraph(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data.'))
