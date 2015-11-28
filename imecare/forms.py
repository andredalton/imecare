# coding=utf-8

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
    senha = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())
    senha2 = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput(), label='Repetir senha')

    class Meta:
        model = Paciente
        fields = (
            'nome',
            'rg',
            'cpf',
            'senha',
            'senha2',
            'email',
            'tipo_sanguineo',
            'data_nascimento'
        )

    def clean(self):
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')

        if senha and senha != senha2:
            self.add_error('senha', "As senhas devem ser iguais.")
            self.add_error('senha2', "As senhas devem ser iguais.")
            raise forms.ValidationError("As senhas não são iguais.")

        return self.cleaned_data