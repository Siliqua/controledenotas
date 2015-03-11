from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'controledenotas.views.home', name='home'),
    # url(r'^controledenotas/', include('controledenotas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


   url(r'^$', 'medias.views.index'),
   url(r'editar/(?P<id_disciplina>\d+)/$', 'medias.views.disciplina'),
   url(r'excluir/(?P<id_disciplina>\d+)/$', 'medias.views.excluir'),
   url(r'adicionar/$', 'medias.views.adicionar'),
   url(r'gerarpdf/$', 'medias.views.gerarpdf'),
   url(r'pdfhtml/$', 'medias.views.html_view')
)
