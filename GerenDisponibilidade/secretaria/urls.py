from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('secretaria.views',
    url(r'^$', 'listaTipos', name='listaTipos'),
    url(r'^novo-tipo-de-sala/$', 'addTipoDeSala', name='addTipoDeSala'),
        
)
