from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['materia', 'nota']  # 'usuario' se manejará en la vista
        widgets = {
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1',
                'min': '0',
                'max': '20'
            }),
        }
        labels = {
            'materia': 'Materia',
            'nota': 'Nota',
        }
