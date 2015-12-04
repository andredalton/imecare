# coding=utf-8

from django.contrib.auth.decorators import login_required
from ..models import Pessoa, Procedimento, Solicita, Realiza
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from time import strftime


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
            import hashlib
            cpf_paciente = request.user.username
            data_realizacao = request.POST['data_realizacao'] if 'data_realizacao' in request.POST else strftime("%Y-%m-%d")
            string = cpf_paciente + data_realizacao + procedimento.nome
            string = string.encode('utf-8')
            code = hashlib.md5(string).hexdigest()
            realiza = Realiza()
            realiza.procedimento = procedimento
            realiza.solicitacao = solicita
            realiza.paciente = paciente
            realiza.data = data_realizacao
            realiza.save()

            fields = {
                'id': code,
                'data': str(realiza.data),
                'horario': str(realiza.horario)
            }
            campo_count = int(request.POST['campo_count'])
            for i in range(1, campo_count+1):
                campo = request.POST["campo%d" % i].encode('utf-8')
                conteudo = request.POST["conteudo%d" % i].encode('utf-8')
                unidade = request.POST["unidade%d" % i].encode('utf-8')
                fields["%s_campo" % campo] = conteudo
                if len(unidade) > 0:
                    fields["%s_unidade" % campo] = unidade

            from pymongo import MongoClient
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