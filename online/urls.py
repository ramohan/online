from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'ticketbooking.views.login'),
    url(r'^signup','ticketbooking.views.signup'),
)
