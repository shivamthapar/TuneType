from django.conf.urls import patterns, include, url

urlpatterns = patterns('battle.views',
    url(r'^(?P<artist>[a-zA-Z0-9\-+]+)/(?P<song>[a-zA-Z0-9\-+]+)/lyrics/$', 'lyrics'),

)