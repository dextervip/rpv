from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('professor.views',
    url(r'^$', 'home', name='home'),
        
)
