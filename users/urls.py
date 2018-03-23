from django.conf.urls import include,url
from django.contrib.auth.views import login

from . import views
from views import UserLogin, UserRegistration, UserMe, UserList, UserLogout

urlpatterns = [
    url(r'^login/$',UserLogin.as_view(),name='login'),
    url(r'^register/$', UserRegistration.as_view(), name='register'),
    url(r'^logout/$', UserLogout.as_view(), name='logout_view'),
    url(r'^users/me/$',UserMe.as_view(),name='index'),
    url(r'^users/$', UserList.as_view() ,name='all_users'),
]
