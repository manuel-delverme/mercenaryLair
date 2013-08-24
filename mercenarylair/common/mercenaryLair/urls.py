from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^display.php/$', 'display.views.index'),
    url(r'^display.php/(?P<type_filter>\w+)/', 'display.views.index'),
    url(r'^detail.php$', 'display.views.index'),
    url(r'^detail.php/(?P<service_id>\d+)/', 'display.views.detail'),
    url(r'^update.php/(?P<service_id>\d+)/', 'display.views.update'),
    url(r'^post/$', 'display.views.post'),
    url(r'^account/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mercenaryLair.views.index'),
    )
