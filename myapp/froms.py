from django import forms
from myapp.models import School, Student
from django.core import validators

class SchoolForms(forms.ModelForm):
    Student_name =  forms.CharField()
    Student_phno = forms.CharField()
    class Meta:
        model = School
        fields = '__all__'
