# coding=utf-8

from django.contrib.auth.decorators import login_required
from ..forms import TrocarSenhaForm
from ..models import Pessoa, Atendimento, Realiza
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext

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
def meus_procedimentos(request):
    realizados = Realiza.objects.filter(paciente=request.user).order_by('-data', '-horario')
    context = {'realizados': realizados}
    return render_to_response('meus_procedimentos.html',
                              context,
                              context_instance=RequestContext(request))