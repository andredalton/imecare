# coding=utf-8
from socket import p

from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import PacienteForm, MedicoForm
from models import Paciente, Medico
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

def home(request):
    context = {}
    return render_to_response('base.html',
                       context,
                       context_instance=RequestContext(request))


def login_user(request, tipo):
    logout(request)
    if request.POST:
        username = request.POST['cpf'] if tipo == 'paciente' else request.POST['cpf']
        password = request.POST['senha']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def novo_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        cpf = request.POST['cpf']
        senha = request.POST['senha']
        p = Paciente.objects.get(username=cpf)
        p.set_password(senha)
        p.save()
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
        m = Medico.objects.get(username=cpf)
        m.set_password(senha)
        m.is_staff = True
        m.save()
        user = authenticate(username=cpf, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
        return HttpResponseRedirect('/')
    context = {'form': form}
    return render_to_response('novo_medico.html',
                              context,
                              context_instance=RequestContext(request))


