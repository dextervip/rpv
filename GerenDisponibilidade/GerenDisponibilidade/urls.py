from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^$', include('geral.urls')),
    (r'^geral/', include('geral.urls', namespace='geral')),
    #(r'^page-login/$', 'geral.views.pageLogin'),
    #(r'^sobre/$', 'geral.views.sobre'),
    #(r'^contato/$', 'geral.views.contato'),
    (r'^coordenador-home/$', 'coordenador.views.home'),
    (r'^secretaria/', include('secretaria.urls', namespace='secretaria')),
    (r'^professor/', include('professor.urls', namespace='professor')),
    (r'^coordenador/', include('coordenador.urls', namespace='coordenador')),
    #(r'^lista/$', 'disciplinas.views.lista'),
    #(r'^addDisciplina/$', 'disciplinas.views.addDisciplina'),
    (r'^disciplina/(?P<nr_disci>\d+)/$', "disciplinas.views.disciplina"),
    (r'^removerDiscip/(?P<nr_discp>\d+)/$', "disciplinas.views.removerDiscip"),
    (r'^editarDiscip/(?P<nr_disci>\d+)/$', 'disciplinas.views.editarDiscip'),
    (r'^pesquisaDiscip/$', 'disciplinas.views.pesquisaDiscip'),
    (r'^secretaria/tipos_de_sala/(?P<nr_tipo>\d+)/$', "secretaria.views.tipoDeSala"),
    (r'^editarTipoSala/(?P<nr_tipo>\d+)/$', 'secretaria.views.editarTipoSala'),
    (r'^removerTipoSala/(?P<nr_tipo>\d+)/$', "secretaria.views.removerTipoSala"),
    (r'^pesquisaTipoSala/$', 'secretaria.views.pesquisaTipoSala'),
    (r'^secretaria/sala/(?P<nr_sala>\d+)/$', "secretaria.views.s_sala"),
    (r'^editarSala/(?P<nr_sala>\d+)/$', 'secretaria.views.editarSala'),
    (r'^removerSala/(?P<nr_sala>\d+)/$', "secretaria.views.removerSala"),
    (r'^pesquisaSala/$', 'secretaria.views.pesquisaSala'),
    (r'^lista-disciplinas/', include('disciplinas.urls', namespace='disciplinas')),
    #(?<paramPesq>\w+)/


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
