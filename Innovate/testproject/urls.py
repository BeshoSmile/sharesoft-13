from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^email/', 'www.views.sendemail'),
    url(r'^Contact/', 'www.views.view_contact_us'),
    url(r'^base/', 'www.views.render_base'),


    url(r'^base/', 'www.views.render_base'),
    url(r'^radio/', 'www.views.render_radioAds'),
    url(r'^sorl/', 'www.views.render_app_test'),



)
