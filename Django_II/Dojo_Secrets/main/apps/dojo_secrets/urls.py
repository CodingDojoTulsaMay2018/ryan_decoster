from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^profile$', views.profile),
    url(r'^secret$', views.secret),
    url(r'^popular$', views.popular),
    url(r'^logout$', views.logout),
    url(r'^delete$', views.delete),
    url(r'^delete_2$', views.delete_2),
    url(r'^like$', views.like),
    url(r'^like_2$', views.like_2),
] 