from django.core.management.base import BaseCommand
from fabio.models import Petition
from datetime import datetime
from random import choice, randint
import faker  # You'll need to install the "Faker" library

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        status_choices = ['pending', 'approved', 'rejected']
        subjects_choices = ['Subject A', 'Subject B', 'Subject C']
        petitions_to_create = 10  # Change this as needed

        for _ in range(petitions_to_create):
            petition = Petition.objects.create(
                ci=fake.unique.random_int(min=1000000000, max=9999999999),  # Generate a unique random CI
                email=fake.email(),
                student_name=fake.name(),
                subjects=', '.join(fake.random.choices(subjects_choices, k=randint(1, 3))),
                hours=fake.random_element(elements=('5 hours per week', '10 hours per week')),
                date=fake.date_of_birth(minimum_age=18, maximum_age=30),  # Random date within an age range
                petition_text=fake.text(),
                status=choice(status_choices),
                pdf_file=None,  # You can handle file uploads separately if needed
                observations=fake.text() if choice([True, False]) else None,  # Optional field
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully created petition: {petition.pk}'))
