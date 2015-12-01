# coding=utf-8
from socket import p

from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


from forms import PacienteForm, MedicoForm, AtendimentoForm, \
    TrocarSenhaForm, SolicitaForm, DiagnosticadaForm, PacienteSelectForm
from models import Pessoa, Atendimento, Procedimento, Doenca, DiagnosticadaEm
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
    if request.POST:
        cpf = request.POST['cpf']
        try:
            paciente = Pessoa.objects.get(cpf=cpf)
        except Pessoa.DoesNotExist:
            paciente = None

        if paciente is not None:
            nsolicita = 20
            proc_count = int(request.POST['proc_count']) if request.POST['proc_count'] else 1
            doenca_count = int(request.POST['doenca_count']) if request.POST['doenca_count'] else 1
            atendimento = AtendimentoForm(request.user, paciente, request.POST or None, prefix='atendimento')
            solicitacoes = []
            diagnosticadas = []
            for i in xrange(nsolicita):
                solicitacoes.append(SolicitaForm(request.POST or None, prefix='solicita'+str(i)))
                diagnosticadas.append(DiagnosticadaForm(request.POST or None, prefix='doenca'+str(i)))
            # expositores = Expositor.objects.filter(user__is_active=block).all().order_by('nome')
            doencas_ativas = DiagnosticadaEm.objects.filter(paciente=paciente, fim__isnull=True)
            doencas_curadas = DiagnosticadaEm.objects.filter(paciente=paciente, fim__isnull=False)
            procedimentos = Procedimento.objects.all()
            doencas = Doenca.objects.all()

            if request.POST['proc_count'] != "":
                if atendimento.is_valid():
                    atendimento = atendimento.save()
                    for solicita in solicitacoes:
                        solicita.set_atendimento(atendimento)
                        if solicita.is_valid():
                            solicita.save()
                    for diagnosticada in diagnosticadas:
                        diagnosticada.set_atendimento(atendimento)
                        if diagnosticada.is_valid():
                            diagnosticada.save()
                    return HttpResponseRedirect('/atendimento/novo/')

            context = {
                'paciente': paciente,
                'proc_count': proc_count,
                'doenca_count': doenca_count,
                'atendimento': atendimento,
                'solicitacoes': solicitacoes,
                'diagnosticadas': diagnosticadas,
                'procedimentos': procedimentos,
                'doencas': doencas,
                'doencas_ativas': doencas_ativas,
                'doencas_curadas': doencas_curadas,
            }

            return render_to_response('novo_atendimento.html',
                                      context,
                                      context_instance=RequestContext(request))
    form = PacienteSelectForm(request.POST or None)
    context = {'form': form}
    return render_to_response('inicio_atendimento.html',
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
