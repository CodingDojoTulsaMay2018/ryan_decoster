from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^loginCheck$', views.loginCheck),
    url(r'^register$', views.register),
    url(r'^create$', views.create),
    url(r'^dashboard/admin$', views.admin),
    url(r'^users/new$', views.new), 
    url(r'^users/createNew$', views.createNew), 
    url(r'^dashboard$', views.dashboard),
    url(r'^users/(?P<id>\d+)/message$', views.message),
    url(r'^users/(?P<id>\d+)/comment$', views.comment),
    url(r'^users/(?P<id>\d+)/edit$', views.edit), 
    url(r'^users/(?P<id>\d+)/adminEdit$', views.adminEdit),
    url(r'^users/(?P<id>\d+)/updateDescription$', views.updateDescription), 
    url(r'^users/(?P<id>\d+)/updateInfo$', views.updateInfo), 
    url(r'^users/(?P<id>\d+)/adminUpdateInfo$', views.adminUpdateInfo), 
    url(r'^users/(?P<id>\d+)/adminUpdatePassword$', views.adminUpdatePassword), 
    url(r'^users/(?P<id>\d+)/updatePassword$', views.updatePassword),
    url(r'^users/(?P<id>\d+)/show$', views.show),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^logout$', views.logout),
]