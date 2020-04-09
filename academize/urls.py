from django.conf.urls import include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# 
admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r"^admin/", admin.site.urls, name="admin"),
    # url(r'^$', 'academize.views.home', name='home'),


]
    # Examples:
    # url(r'^$', 'academize.views.home', name='home'),
    # url(r'^academize/', include('academize.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # 
