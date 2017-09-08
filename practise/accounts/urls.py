from django.conf.urls import url,include

from accounts.views import login
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns=[
	url(r'^$', views.login, name='login'),
	url(r'^prof/$', views.prof, name='prof'),
	url(r'^login/$', auth_views.login, {'template_name': 'accounts/base.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]