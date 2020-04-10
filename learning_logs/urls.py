"""urls for leanring_logs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    
    #all topics
    url(r'^topics/$',views.topics,name='topics'),
    
    #topic details  P -> upper case.
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic, name='topic'),
    
    #create topic page
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    
    #create entry for topics
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry, name='new_entry'),
    
    #edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]