from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.dojo_ninjas.urls')),
    url(r'^book_authors/', include('apps.book_authors.urls')),
]
