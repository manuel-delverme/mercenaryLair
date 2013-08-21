from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^display.php$', 'display.views.index'),
    url(r'^detail.php$', 'display.views.index'),
    url(r'^detail.php/(?P<service_id>\d+)/', 'display.views.detail'),
    url(r'^$', 'mercenaryLair.views.index'),
)
