# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import PacienteForm
from models import Paciente
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


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['cpf']
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