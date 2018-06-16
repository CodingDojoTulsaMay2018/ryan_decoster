from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.register),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
] 