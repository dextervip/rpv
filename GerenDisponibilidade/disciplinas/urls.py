from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('disciplinas.views',
    url(r'^$', 'lista', name='lista'),
    url(r'^addDisciplina/$', 'addDisciplina', name='addDisciplina'),
   # url(r'^attInfoDisciplinas/$', 'attInfoDisciplinas', name='attInfoDisciplinas'),
    
)
