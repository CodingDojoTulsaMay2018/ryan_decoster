from django.conf.urls import url, include
from django.conf.urls import url

urlpatterns = [
    url(r'^', include('apps.first_app.urls')),
    url(r'^first_app/', include('apps.first_app.urls'))
]
