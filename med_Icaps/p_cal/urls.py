from django.conf.urls import include, url
from django.contrib import admin

from . import views

import calendarium

from django.contrib import auth

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login', views.login_user),
    url(r'^calendar', include('calendarium.urls')),
    url(r'', views.index, name='Index'),

]
