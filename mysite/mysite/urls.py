# urls.py
from django.conf.urls import patterns, include, url
from myapp.api import *

group_resource = GroupResource()
hotel_resource = HotelResource()
user_resource = UserResource()
user_access_resource = UserAccessResource()
access_token_resource = AccessTokenResource()
room_rates_resource = RoomRatesResource()

urlpatterns = patterns('',
    (r'^api/', include(group_resource.urls)),
    (r'^api/', include(hotel_resource.urls)),
    (r'^api/', include(user_resource.urls)),
    (r'^api/', include(user_access_resource.urls)),
    (r'^api/', include(access_token_resource.urls)),
    (r'^api/', include(room_rates_resource.urls)),
)
