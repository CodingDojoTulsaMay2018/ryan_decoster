from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.blogs_app.urls')),   
]
