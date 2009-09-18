#coding: utf-8

import os
from settings import ROOT_PATH
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #admin
    (r'^admin/(.*)', admin.site.root),

    #main
    (r'^$', 'urlShortener.main.views.index'),
    (r'^(?P<id>\w+)/?$', 'urlShortener.main.views.long_url'),
    (r'^get/short/url/?$', 'urlShortener.main.views.short_url'),

    #media files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(ROOT_PATH, 'media')}),
)
