from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('secretaria.views',
    url(r'^listaTipos$', 'listaTipos', name='listaTipos'),
    url(r'^$', 'listaSalas', name='listaSalas'),
    url(r'^novo-tipo-de-sala/$', 'addTipoDeSala', name='addTipoDeSala'),
    url(r'^novaSala/$', 'addSala', name='addSala'),
        
)
