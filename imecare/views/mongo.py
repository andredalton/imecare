# coding=utf-8

from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Pessoa, Procedimento, Solicita, Realiza
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from time import strftime
from pymongo import MongoClient
import hashlib

@login_required
def insere_procedimento(request):
    paciente = Pessoa.objects.get(cpf=request.user.username)
    loop = range(40)
    valid = False
    solicita = None
    solicita_id = "-1"
    if request.POST:
        solicita_id = request.POST['solicitacao_id']
        if solicita_id != "-1":
            try:
                solicita = Solicita.objects.get(id=solicita_id, atendimento__paciente=request.user)
                procedimento = solicita.procedimento
                valid = True
            except Solicita.DoesNotExist:
                pass
        else:
            proc_nome = request.POST['proc_nome']
            try:
                procedimento = Procedimento.objects.get(nome=proc_nome)
                valid = True
            except Procedimento.DoesNotExist:
                pass
        if 'campo_count' in request.POST:
            cpf_paciente = request.user.username
            data_realizacao = request.POST['data_realizacao'] if 'data_realizacao' in request.POST else strftime("%Y-%m-%d")
            realiza = Realiza()
            realiza.procedimento = procedimento
            realiza.solicitacao = solicita
            realiza.paciente = paciente
            realiza.data = data_realizacao
            realiza.save()

            fields = {
                'sql_id': realiza.id,
                'data': str(realiza.data),
                'horario': str(realiza.horario),
                'campos': []
            }
            campo_count = int(request.POST['campo_count'])
            for i in range(1, campo_count+1):
                campo = request.POST["campo%d" % i].encode('utf-8')
                conteudo = request.POST["conteudo%d" % i].encode('utf-8')
                unidade = request.POST["unidade%d" % i].encode('utf-8')
                fields['campos'].append({
                    'nome': campo,
                    'conteudo': conteudo,
                    'unidade': unidade
                })
                fields["%s_conteudo" % campo] = conteudo
                fields["%s_unidade" % campo] = unidade
            client = MongoClient()
            db = client.test
            db.realiza.save(fields)
            client.close()
            return HttpResponseRedirect(".")
    if valid:
        context = {'solicitacao': solicita_id, 'procedimento': procedimento, 'loop': loop}
    else:
        procedimentos = Procedimento.objects.all()
        solicita = Solicita.objects.filter(atendimento__paciente=request.user).order_by('-atendimento__data', '-atendimento__horario')
        context = {'solicitacoes': solicita, 'procedimentos': procedimentos}
    return render_to_response('novo_procedimento.html',
                              context,
                              context_instance=RequestContext(request))

@login_required
def visualiza_procedimento(request, id):
    try:
        realiza = Realiza.objects.get(id=id)
    except Realiza.DoesNotExist:
        return HttpResponseRedirect("/404/")
    if realiza.paciente.cpf == request.user.username or request.user.is_staff:
        client = MongoClient()
        db = client.test
        conteudo = db.realiza.find_one({'sql_id': int(id)})
        client.close()
        context = {'realizacao': realiza, 'conteudo': conteudo, }
        return render_to_response('visualiza_procedimento.html',
                                  context,
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/404/")

@login_required
@user_passes_test(lambda u: u.is_staff)
def pesquisa(request):
    realizados = None
    loop = range(1, 41)
    if request.POST:
        realizados = []
        if request.POST['and'] == 'and':
            campo_count = int(request.POST['campo_count'])
            fields = {'$and': []}
            for i in range(1, campo_count+1):
                campo = request.POST["campo%d" % i].encode('utf-8')
                conteudo = request.POST["conteudo%d" % i].encode('utf-8')
                unidade = request.POST["unidade%d" % i].encode('utf-8')
                fields['$and'].append({"%s_conteudo" % campo: conteudo})
                fields['$and'].append({"%s_unidade" % campo: unidade})
            client = MongoClient()
            db = client.test
            resultados = db.realiza.find(fields)
            client.close()
            for resultado in resultados:
                realizados.append(Realiza.objects.get(id=resultado['sql_id']))
        else:
            campo_count = int(request.POST['campo_count'])
            fields = {'$or': []}
            for i in range(1, campo_count+1):
                campo = request.POST["campo%d" % i].encode('utf-8')
                conteudo = request.POST["conteudo%d" % i].encode('utf-8')
                unidade = request.POST["unidade%d" % i].encode('utf-8')
                fields['$or'].append({"$and": [
                    {"%s_conteudo" % campo: conteudo},
                    {"%s_unidade" % campo: unidade}
                ]})
            client = MongoClient()
            db = client.test
            resultados = db.realiza.find(fields)
            client.close()
            for resultado in resultados:
                realizados.append(Realiza.objects.get(id=resultado['sql_id']))
    context = {'loop': loop, 'realizados': realizados}
    return render_to_response('pesquisa.html',
                              context,
                              context_instance=RequestContext(request))