# coding=utf-8

from django import forms
from models import verifica_cpf, Pessoa, Atendimento


def verificaPessoa(form, senha1, senha2, cpf):
    if not verifica_cpf(cpf):
        form.add_error('cpf', "Digite um CPF válido.")
        raise forms.ValidationError("CPF inválido.")

    if senha1 and senha1 != senha2:
        form.add_error('senha', "As senhas devem ser iguais.")
        form.add_error('senha2', "As senhas devem ser iguais.")
        raise forms.ValidationError("As senhas não são iguais.")


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
        model = Pessoa
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
        verificaPessoa(self, senha, senha2, cpf)
        self.instance.set_password(senha)
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
        model = Pessoa
        fields = (
            'nome',
            'rg',
            'cpf',
            'crm',
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
        verificaPessoa(self, senha, senha2, cpf)
        self.instance.is_staff = True
        self.instance.set_password(senha)
        return self.cleaned_data


class AtendimentoForm(forms.ModelForm):
    cpf = forms.CharField(max_length=30, label='CPF do paciente', widget=forms.TextInput(attrs=
    {
        'class': 'cpf'
    }))

    class Meta:
        model = Atendimento
        fields = (
            'cpf',
            'comentarios',
        )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AtendimentoForm, self).__init__(*args, **kwargs)

    def clean(self):
        cpf = self.cleaned_data.get('cpf')
        paciente = Pessoa.objects.get(cpf=cpf)
        medico = Pessoa.objects.get(cpf=self.user.username)
        self.instance.paciente = paciente
        self.instance.medico = medico
        return self.cleaned_data
