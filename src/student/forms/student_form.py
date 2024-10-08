from django import forms
from ..models.student_model import StudentModel


class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentModel
        exclude = ['status', 'active']

        widgets ={
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
 