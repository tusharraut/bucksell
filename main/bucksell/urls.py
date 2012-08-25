from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import registration
urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'test1.views.home', name='home'),
    # url(r'^test1/', include('test1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user_profile.urls')),
    url(r'^ads/', include('ads.urls')),
    url(r'^items/', include('items.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^universities/', include('universities.urls')),
    url(r'^', include('registration.urls')),

)