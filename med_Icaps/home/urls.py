from django.conf.urls import include, url

from home import views

urlpatterns = [
    url(r'^home/', include('home.urls')),
    url(r'^calendar/', include('calendarium.urls')),
]

