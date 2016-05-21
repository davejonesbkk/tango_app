from django.conf.urls import url 
from django.contrib import admin

from . import views

app_name='tango'

urlpatterns = [
	#/tango/
	url(r'^$', views.IndexView.as_view(), name='index'),
	#/tango/about
	url(r'^about/', views.about, name='about'),
	#/tango/5
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	#/tango/5/results
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	#/tango/5/results/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

	
]

