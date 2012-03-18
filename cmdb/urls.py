from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^query/(?P<ip>(?:\w+\.)+\w+)/$','cmdb.webservice.views.queryInfoByIp2Web'),
    # Examples:
    # url(r'^$', 'cmdb.views.home', name='home'),
    # url(r'^cmdb/', include('cmdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
