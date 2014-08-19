from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
#from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url (r'^add_user/$', 'myapp.views.add_user.page', name="add_user"),
    url(r'^logout/$', 'myapp.views.logout.page', name="user_logout"),
    url(r'^login/$', 'myapp.views.login.page', name="user_login"),
    #url(r'^$', login_required(TemplateView.as_view(template_name='jp/index.html')), name="index"),
    url(r'^$', 'myapp.views.index.page', name="index"),
    url(r'^admin/', include(admin.site.urls)),
)
