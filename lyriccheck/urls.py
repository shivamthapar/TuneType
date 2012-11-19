from django.conf.urls import patterns, include, url

urlpatterns = patterns('lyriccheck.views',
    url(r'^$', 'index'),
    url(r'^(?P<artist>[a-zA-Z0-9\-+]+)/(?P<song>[a-zA-Z0-9\-+]+)/lyrics/$', 'lyrics'),

)