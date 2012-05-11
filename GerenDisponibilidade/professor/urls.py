from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('professor.views',
    url(r'^$', 'home', name='home'),
    url(r'^adicionar-compromisso$', 'adicionarCompromisso', name='adicionarCompromisso'),
    url(r'^visualizar-compromisso/(?P<id>\d{1,10})$', 'visualizarCompromisso', name='visualizarCompromisso'),
    url(r'^get-compromissos$', 'getCompromissos', name='getCompromissos'),
        
)
