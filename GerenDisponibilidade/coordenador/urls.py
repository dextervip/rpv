from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('coordenador.views',
     url(r'^montarGradeAula$', 'montarGradeAula', name='montarGradeAula'),
)
