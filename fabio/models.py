from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Petition(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )
    ci = models.CharField(max_length=10)
    email = models.EmailField()
    student_name = models.CharField(max_length=100)
    subjects = models.TextField()
    hours = models.CharField(max_length=50)
    date = models.DateField()
    petition_text = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    pdf_file = models.FileField(upload_to='petition_pdfs/', blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    


# class Petition(models.Model):
#     student_name = models.CharField(max_length=100)
#     petition_text = models.TextField()
#     status = models.CharField(max_length=10)
