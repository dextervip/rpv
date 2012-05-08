from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('professor.views',
    url(r'^$', 'home', name='home'),
    url(r'^adicionar-compromisso$', 'adicionarCompromisso', name='adicionarCompromisso'),
    url(r'^get-compromissos$', 'getCompromissos', name='getCompromissos'),
        
)
