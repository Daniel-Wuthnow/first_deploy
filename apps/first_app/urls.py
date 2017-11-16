from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^create', views.create),
	url(r'^new', views.new),
	url(r'^$', views.index)     # This line has changed!
]