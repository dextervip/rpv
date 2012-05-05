from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GerenDisponibilidade.views.home', name='home'),
    # url(r'^GerenDisponibilidade/', include('GerenDisponibilidade.foo.urls')),
    (r'^$', 'geral.views.home'),
    (r'^lista-disciplinas/', include('disciplinas.urls', namespace='disciplinas')),
    (r'^secretaria/', include('secretaria.urls', namespace='secretaria')),
    #(r'^lista/$', 'disciplinas.views.lista'),
    #(r'^addDisciplina/$', 'disciplinas.views.addDisciplina'),
    (r'^disciplina/(?P<nr_disci>\d+)/$', "disciplinas.views.disciplina"),
    (r'^removerDiscip/(?P<nr_discp>\d+)/$', "disciplinas.views.removerDiscip"),
    (r'^editarDiscip/(?P<nr_disci>\d+)/$', 'disciplinas.views.editarDiscip'),
    (r'^pesquisaDiscip/$', 'disciplinas.views.pesquisaDiscip'),
    #(?<paramPesq>\w+)/


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
