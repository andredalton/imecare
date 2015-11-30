# coding=utf-8

from django import forms
from models import verifica_cpf, Pessoa, Atendimento, Solicita, Procedimento
from django.contrib.auth import authenticate, login

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
        try:
            paciente = Pessoa.objects.get(cpf=cpf)
        except Pessoa.DoesNotExist:
            self.add_error('cpf', "Este CPF não está cadastrado.")
            raise forms.ValidationError("CPF inválido.")
        medico = Pessoa.objects.get(cpf=self.user.username)
        self.instance.paciente = paciente
        self.instance.medico = medico
        return self.cleaned_data

class TrocarSenhaForm(forms.Form):
    senha_antiga = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())
    nova_senha = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())
    repetir_senha = forms.CharField(max_length=30, min_length=5, widget=forms.PasswordInput())

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(TrocarSenhaForm, self).__init__(*args, **kwargs)

    def clean(self):
        senha_antiga = self.cleaned_data.get('senha_antiga')
        nova_senha = self.cleaned_data.get('nova_senha')
        repetir_senha = self.cleaned_data.get('repetir_senha')

        if nova_senha != repetir_senha:
            self.add_error('nova_senha', "As senhas não são iguais.")
            self.add_error('repetir_senha', "As senhas não são iguais.")
        user = authenticate(username=self.request.user.username, password=senha_antiga)

        if user and nova_senha == repetir_senha:
            return self.cleaned_data
        else:
            self.add_error('senha_antiga', "A senha não confere.")
        raise forms.ValidationError("Erro na autenticação.")

    def save(self):
        senha_antiga = self.cleaned_data.get('senha_antiga')
        nova_senha = self.cleaned_data.get('nova_senha')
        user = authenticate(username=self.request.user.username, password=senha_antiga)
        user.set_password(nova_senha)
        user.save()
        login(self.request, user)


class SolicitaForm(forms.ModelForm):
    procedimento_nome = forms.CharField(
        max_length=100,
        label='procedimento',
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'proc_nome'}
        )
    )

    class Meta:
        model = Solicita
        fields = (
            'procedimento_nome',
            'detalhes',
        )

    def set_atendimento(self, atendimento):
        self.instance.atendimento = atendimento

    def clean(self):
        procedimento_nome = self.cleaned_data.get('procedimento_nome')

        try:
            procedimento = Procedimento.objects.get(nome=procedimento_nome)
        except Procedimento.DoesNotExist:
            procedimento = None
        if procedimento:
            self.instance.procedimento = procedimento
            return self.cleaned_data
        if len(procedimento_nome) > 0:
            self.add_error('procedimento_nome', "Digite um nome de procedimento válido.")
        raise forms.ValidationError("Procedimento inválido.")