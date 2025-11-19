from django.forms import ModelForm, TextInput, EmailInput

from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields ='__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'}),
        }