from django import forms
from models import Paciente, Telefone

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = (
            'numero',
            'contato',
            'parentesco'
        )

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = (
            'nome',
            'rg',
            'cpf',
            'email',
            'tipo_sanguineo',
            'data_nascimento'
        )