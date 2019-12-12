

from django.conf.urls import url
from django.contrib import admin
from app import views


urlpatterns = [
	#url(r'^admin/', admin.site.urls),
	url(r'^$', views.f1),
	url(r'^home2/', views.f2),
	url(r'^home3/', views.f3),
	url(r'^home4/', views.f4),
]
