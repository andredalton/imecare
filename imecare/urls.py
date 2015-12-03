"""imecare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    url(r'^' + settings.SERVER_FOLDER + 'admin/', include(admin.site.urls)),
    url(r'^' + settings.SERVER_FOLDER + '$', 'imecare.views.home', name='home'),
    url(r'^' + settings.SERVER_FOLDER + 'novo_paciente/?$', 'imecare.views.novo_paciente', name='registro_paciente'),
    url(r'^' + settings.SERVER_FOLDER + 'novo_medico/?$', 'imecare.views.novo_medico', name='registro_medico'),
    url(r'^' + settings.SERVER_FOLDER + 'entrar/(?P<tipo>\w{0,10})', 'imecare.views.login_user', name='login'),
    url(r'^' + settings.SERVER_FOLDER + 'sair/?', 'imecare.views.logout_user', name='logout'),
    url(r'^' + settings.SERVER_FOLDER + 'atendimento/novo/?', 'imecare.views.novo_atendimento', name='registro_atendimento'),
    url(r'^' + settings.SERVER_FOLDER + 'atendimentos/?', 'imecare.views.atendimentos', name='atendimentos'),
    url(r'^' + settings.SERVER_FOLDER + 'trocar_senha/?', 'imecare.views.trocar_senha', name='trocar_senha'),
    url(r'^' + settings.SERVER_FOLDER + 'atendimento/curar/(?P<cpf>[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2})/(?P<id>\d+)/?', 'imecare.views.curar_doenca', name='curar_doenca'),




    url(r'^teste/?', 'imecare.views.teste', name='teste'),

]
