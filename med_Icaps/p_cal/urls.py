from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar', views.calendar, name="Calendar"),
    url(r'^login/', views.login, name="Login"),
	url(r'', views.index, name='Index'),
]
