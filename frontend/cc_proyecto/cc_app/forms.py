from django import forms
from .models import Repo

class RepoForm(forms.Form):
    nombre_repo = forms.CharField(
        label='Nombre del repositorio',
        required=False,
        widget=forms.TextInput(
            attrs=({
                'placeholder': 'Nombre del repositorio',
                "id":"nombre_repo",
                "help_text":"Recomendado completar este campo"
            })
        ),
    )
    url_repo = forms.URLField(
        label='URL del repositorio',
        widget=forms.Textarea (
            attrs=({
                'placeholder': 'Ingrese la(s) URL(s) de los repositorios',
                "id":"url_repo",
                "help_text":"Campo obligatorio"
            })
        ),
    )

    class Meta:
        modelo = Repo
