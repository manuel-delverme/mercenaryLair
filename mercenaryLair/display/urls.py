from django.conf.urls import patterns, url

urlpatterns = patterns('display.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    )
