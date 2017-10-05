from django.conf.urls import url,include
from simplelogin import views

urlpatterns = [ 
    url(r'^home_simple/$', views.home_simple, name='home_simple'),
    url(r'^login_simple/$', views.login_simple, name='login_simple'),
    url(r'^my_view/$',views.my_view,name="my_view"),
    url(r'^add_contact/$',views.add_contact,name="add_contact"),
    url(r'^edit_contact/$',views.edit_contact,name="edit_contact"),
    url(r'^delete_contact/$',views.delete_contact,name="delete_contact"),
    url(r'^reg_simple/$',views.reg_simple,name="reg_simple"),
    url(r'^logout_simple/$', views.logout_simple, name='logout_simple'),
    url(r'^user_profile/$',views.user_profile,name='user_profile'),
    url(r'^edit_user_profile/$',views.edit_user_profile,name='edit_user_profile'),
    url(r'^send_message/$',views.send_message,name='send_message'),
    url(r'^user_messages/$',views.user_messages,name='user_messages'),
    url(r'^send_message_by_number/$',views.send_message_by_number,name='send_message_by_number'),
    url(r'^user_message_thread/$',views.user_message_thread,name='user_message_thread'),
    url(r'^send_message_by_thread/$',views.send_message_by_thread,name='send_message_by_thread')
    ]