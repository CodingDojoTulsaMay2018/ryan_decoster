from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^users/$', views.index),                  # Display all users

    url(r'^users/new$', views.new),                 # Displays a form allowing to create a new                                                    user

    url(r'^users/(?P<id>\d+)/edit$', views.edit),          # Displays a form allowing to edit a                                                          user with the given id

    url(r'^users/(?P<id>\d+)$', views.show),               # Display the user info with the                                                              given id

    url(r'^users/create$', views.create),           # POST method that should be sent to the                                                      form on the users/new page. Redirect this                                                   to users/<id> once created

    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),    # Remove a particular user with the                                                           given id

    url(r'^users/(?P<id>\d+)/update$', views.update),           # POST method that processes the                                                              users/<id>/edit form. Redirect this to                                                      users/<id> once submitted.
]