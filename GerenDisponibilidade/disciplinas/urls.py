from django.conf.urls.defaults import patterns, url, include


urlpatterns = patterns('disciplinas.views',
    url(r'^$', 'lista', name='lista'),
    url(r'^nova-disciplina/$', 'addDisciplina', name='addDisciplina'),
    #url(r'^(?P<nr_discp>\d+)/$', 'removerDiscip', name='removerDiscip'),
    #url(r'^infos-disciplina/(?P<nr_disci>\d+)/$', 'disciplina', name='disciplina'),
    #url(r'^attInfoDisciplinas/$', 'attInfoDisciplinas', name='attInfoDisciplinas'),
    
)
