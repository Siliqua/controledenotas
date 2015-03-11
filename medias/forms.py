from django import forms
from models import Disciplina
from django.forms import DecimalField

class FormDisciplina(forms.ModelForm):
    nota1 = DecimalField(label="I unidade:")
    nota2 = DecimalField(label="II unidade:")
    nota3 = DecimalField(label="III unidade:")
    class Meta:
        model = Disciplina