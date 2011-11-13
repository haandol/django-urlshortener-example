#coding: utf-8

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    #Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #main
    url(r'^$', 'urlShortener.main.views.index'),
    url(r'^(?P<id>\w+)/?$', 'urlShortener.main.views.long_url'),
    url(r'^get/short/url/?$', 'urlShortener.main.views.short_url'),

    #media files
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT)}),
)
