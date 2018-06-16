from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.blogs_app.urls')),
    url(r'^time_display/', include('apps.time_display.urls')),
    url(r'^random_word/', include('apps.random_word.urls')),
    url(r'^surveys/', include('apps.surveys_app.urls')), 
    url(r'^users/', include('apps.users_app.urls')),   
]
