from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('geral.views',
    url(r'^$', 'pageLogin', name='pageLogin'),
    url(r'^paginaInicial$', 'home', name='home'),
    
)