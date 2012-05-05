from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('secretaria.views',
    url(r'^$', 'home', name='home'),
        
)
