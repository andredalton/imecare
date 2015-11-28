# coding=utf-8

from django import forms
from models import Paciente, Telefone, verifica_cpf, Medico


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
    cpf = forms.CharField(max_length=30, widget=forms.TextInput(attrs=
                                {
                                    'class': 'cpf'
                                }))
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class': 'datepicker'
                                }))

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
        cpf = self.cleaned_data.get('cpf')

        if not verifica_cpf(cpf):
            self.add_error('cpf', "Digite um CPF válido.")
            raise forms.ValidationError("CPF inválido.")

        if senha and senha != senha2:
            self.add_error('senha', "As senhas devem ser iguais.")
            self.add_error('senha2', "As senhas devem ser iguais.")
            raise forms.ValidationError("As senhas não são iguais.")

        return self.cleaned_data

class MedicoForm(forms.ModelForm):
    senha = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())
    senha2 = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput(), label='Repetir senha')
    crm = forms.CharField(max_length=30, label='CRM', widget=forms.TextInput(attrs=
                                {
                                    'class': 'crm'
                                }))
    cpf = forms.CharField(max_length=30, label='CPF', widget=forms.TextInput(attrs=
                                {
                                    'class': 'cpf'
                                }))
    rg = forms.CharField(max_length=30, label='RG')
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class': 'datepicker'
                                }))

    class Meta:
        model = Medico
        fields = (
            'nome',
            'rg',
            'cpf',
            'crm',
            'senha',
            'senha2',
            'email',
            'data_nascimento'
        )

    def clean(self):
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')
        cpf = self.cleaned_data.get('cpf')

        if not verifica_cpf(cpf):
            self.add_error('cpf', "Digite um CPF válido.")
            raise forms.ValidationError("CPF inválido.")

        if senha and senha != senha2:
            self.add_error('senha', "As senhas devem ser iguais.")
            self.add_error('senha2', "As senhas devem ser iguais.")
            raise forms.ValidationError("As senhas não são iguais.")

        return self.cleaned_data