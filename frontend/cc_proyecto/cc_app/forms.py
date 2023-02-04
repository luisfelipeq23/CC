from django import forms
from .models import Repo

class RepoForm(forms.Form):
    url_repo = forms.URLField(
        label='URL del repositorio',
        required=True,
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
