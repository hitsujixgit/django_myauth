from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'myapp.views.index.page', name="index"),
    url(r'^admin/', include(admin.site.urls)),
)
