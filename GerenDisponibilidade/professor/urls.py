from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('professor.views',
    url(r'^$', 'home', name='home'),
    url(r'^adicionar-compromisso$', 'adicionarCompromisso', name='adicionarCompromisso'),
    url(r'^visualizar-compromisso/(?P<id>\d{1,10})$', 'visualizarCompromisso', name='visualizarCompromisso'),
    url(r'^editar-compromisso/(?P<id>\d{1,10})$', 'editarCompromisso', name='editarCompromisso'),
    url(r'^excluir-compromisso/(?P<id>\d{1,10})$', 'excluirCompromisso', name='excluirCompromisso'),
    url(r'^get-compromissos$', 'getCompromissos', name='getCompromissos'),
    url(r'^disponibilidadeAula$', 'disponibilidadeAula', name='disponibilidadeAula'),
    url(r'^informarInteresseDisciplina$', 'informarInteresseDisciplina', name='informarInteresseDisciplina'),
    url(r'^getInteressesDisciplina$', 'getInteressesDisciplina', name='getInteressesDisciplina'),
    url(r'^getDisponibilidadeAula$', 'getDisponibilidadeAula', name='getDisponibilidadeAula'),
        
)
