# coding=utf-8
from socket import p

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test


from forms import PacienteForm, MedicoForm, AtendimentoForm, \
    TrocarSenhaForm, SolicitaForm, DiagnosticadaForm, PacienteSelectForm
from models import Pessoa, Atendimento, Procedimento, Doenca, Diagnosticada, Solicita
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from time import strftime

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
        if request.session.has_key('paciente_cpf'):
            cpf = request.session['paciente_cpf']
        else:
            cpf = request.POST['cpf']
            request.session['paciente_cpf'] = cpf

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
            doencas_ativas = Diagnosticada.objects.filter(paciente=paciente, fim__isnull=True)
            doencas_curadas = Diagnosticada.objects.filter(paciente=paciente, fim__isnull=False)
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
                    del request.session['paciente_cpf']
                    return HttpResponseRedirect('/atendimento/novo/')

            context = {
                'cpf': cpf,
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
    atendimentos = Atendimento.objects.filter(paciente=paciente).order_by('-data', '-horario')
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


@login_required
def insere_procedimento(request):
    valid = False
    if request.POST:
        solicita_id = request.POST['solicitacao_id']
        if solicita_id != "-1":
            try:
                solicita = Solicita.objects.get(id=solicita_id, atendimento__paciente=request.user)
                valid = True
            except Solicita.DoesNotExist:
                pass
        else:
            valid = True

    # from pymongo import MongoClient
    # client = MongoClient()
    # db = client.test
    #
    # result = db.teste.find(
    #     {
    #         "cuisine": "Italian"
    #     }
    # )
    #
    # # Close the MongoDB connection
    # client.close()

    solicita = Solicita.objects.filter(atendimento__paciente=request.user).order_by('-atendimento__data', '-atendimento__horario')


    context = {'solicitacoes': solicita, 'valid': valid}
    return render_to_response('novo_procedimento.html',
                              context,
                              context_instance=RequestContext(request))


@login_required
@user_passes_test(lambda u: u.is_staff)
def curar_doenca(request, cpf, id):
    try:
        diagnostico = Diagnosticada.objects.get(id=id)
        if diagnostico.paciente.cpf == cpf:
            print strftime("%Y-%m-%d")
            if diagnostico.fim is None:
                txt = "Descurar!"
                diagnostico.fim = strftime("%Y-%m-%d")
            else:
                txt = "Curar!"
                diagnostico.fim = None
            diagnostico.save(force_update=True)
        else:
            txt = "Menino mau!"
    except Diagnosticada.DoesNotExist:
        txt = "Menino mau!"
    return HttpResponse('{"txt": "' + txt + '"}', content_type='application/json')

@login_required
@user_passes_test(lambda u: u.is_staff)
def meus_atendimentos(request):
    atendimentos = Atendimento.objects.filter(medico=request.user).order_by('-data')
    context = {'atendimentos': atendimentos}
    return render_to_response('meus_atendimentos.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.is_staff)
def paciente(request, cpf):
    paciente = Pessoa.objects.get(cpf=cpf)
    context = {'paciente': paciente}
    return render_to_response('paciente.html',
                              context,
                              context_instance=RequestContext(request))

