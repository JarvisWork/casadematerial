from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'casa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       
    url(r'^$','casa.core.views.home', name='home'),
    url(r'inscricao/$', 'casa.subscriptions.views.subscribe',name='subscribe'),
    url(r'anuncios/$', 'casa.poster.views.posters',name='posters'),
    
    
    url(r'^admin/', include(admin.site.urls)),
)
