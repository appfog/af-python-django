from django.conf.urls import patterns, url
from views import info


urlpatterns = patterns('', url(r'^$', info))
