# coding=utf-8
from socket import p

from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


from forms import PacienteForm, MedicoForm, AtendimentoForm, TrocarSenhaForm, SolicitaForm
from models import Pessoa, Atendimento, Procedimento
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.db import transaction


def home(request):
    context = {}
    return render_to_response('base.html',
                       context,
                       context_instance=RequestContext(request))


def login_user(request, tipo):
    logout(request)
    if request.POST:
        username = request.POST['cpf']
        password = request.POST['senha']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect('/')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def novo_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        user = authenticate(username=cpf, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render_to_response('novo_paciente.html',
                              context,
                              context_instance=RequestContext(request))


def novo_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        user = authenticate(username=cpf, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render_to_response('novo_medico.html',
                              context,
                              context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_staff)
def novo_atendimento(request):
    nsolicita = 20
    atendimento = AtendimentoForm(request.user, request.POST or None, prefix='atendimento')
    solicitacoes = []
    for i in xrange(nsolicita):
        solicitacoes.append(SolicitaForm(request.POST or None, prefix='solicita'+str(i)))
    procedimentos = Procedimento.objects.all()


    if atendimento.is_valid():
        atendimento = atendimento.save()
        for solicita in solicitacoes:
            solicita.set_atendimento(atendimento)
            if solicita.is_valid():
                solicita.save()
        return HttpResponseRedirect('/atendimento/novo/')
    context = {'atendimento': atendimento, 'solicitacoes': solicitacoes, 'procedimentos': procedimentos}
    return render_to_response('novo_atendimento.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def atendimentos(request):
    paciente = Pessoa.objects.get(cpf=request.user.username)
    atendimentos = Atendimento.objects.filter(paciente=paciente)
    context = {'atendimentos': atendimentos}
    return render_to_response('atendimentos.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def trocar_senha(request):
    form = TrocarSenhaForm(request, request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render_to_response('trocar_senha.html',
                              context,
                              context_instance=RequestContext(request))
