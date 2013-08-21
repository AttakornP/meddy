from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meddy.views.home', name='home'),
    # url(r'^meddy/', include('meddy.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
