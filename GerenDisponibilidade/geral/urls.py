from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('geral.views',
    url(r'^$', 'home', name='home'),
    #url(r'^pageLogin$', 'pageLogin', name='pageLogin'),
    url(r'^sobre$', 'sobre', name= 'sobre'),
    url(r'^contato$', 'contato', name= 'contato'),
    
)