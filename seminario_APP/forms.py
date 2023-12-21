from django import forms
from .models import Inscrito, Institucion

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'
        widgets = {
            'institucion': forms.Select(attrs={'class': 'form-control'}),
        }

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'
