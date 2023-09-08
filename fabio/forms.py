from django import forms
from .models import Petition

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        # fields = ['ci','student_name','desde','hasta','date', 'petition_text', 'pdf_file']
        fields = ['student_name', 'petition_text', 'pdf_file']
        fields = ['ci', 'email', 'student_name', 'subjects', 'hours', 'date', 'petition_text', 'pdf_file']


# class IDSearchForm(forms.Form):
#     id_number = forms.CharField(label='Enter ID', max_length=20)
