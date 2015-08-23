__author__ = 'Diego'

from core import views
from django.conf.urls import patterns, include, url


urlpatterns = [

# DOCUMENTATION
    url(r'^docs/', include('rest_framework_swagger.urls')),

# AUTHENTICATION
    url(r'^auth/$', views.Authenticate.as_view()),
# ME
    url(r'^me', views.UserDetail.as_view(), name='show-me'),
# SCHEDULES
    url(r'^gaps/$', views.GapsList.as_view(), name='show-gaps'),
    url(r'^gaps/(?P<fpk>[a-z]+(\.)?[a-z]+[0-9]*)/$', views.GapsFriendList.as_view(), name='show-friend-gaps'),
    url(r'^gaps/cross/(?P<fpk>[a-z]+(\.)?[a-z]+[0-9]*)/$', views.GapsCross.as_view(), name='show-friend-gaps-cross'),

# FRIEND REQUESTS
    url(r'^requests/sent/$', views.SentFriendRequestList.as_view(), name='sent-friend-requests-list'),
    url(r'^requests/received/$', views.ReceivedFriendRequestsList.as_view(), name='received-friend-requests-list'),
# FRIENDSc
    url(r'^friends/$', views.FriendList.as_view(), name='friend-list'),
    url(r'^friends/(?P<fpk>[a-z]+(\.)?[a-z]+[0-9]*)/$', views.FriendDetail.as_view(), name='friend-detail'),
]

