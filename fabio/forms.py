from django import forms
from .models import RegistroPermisos, RegistroEstudiantes, TodoItem

class RegistroPermisosForm(forms.ModelForm):
    class Meta:
        model = RegistroPermisos
        fields = '__all__'

class RegistroEstudiantesForm(forms.ModelForm):
    class Meta:
        model = RegistroEstudiantes
        fields = '__all__'


# class PetitionForm(forms.ModelForm):
#     class Meta:
#         model = Petition
#         fields = '__all__'
