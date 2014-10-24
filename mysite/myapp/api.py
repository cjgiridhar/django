from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.serializers import Serializer
from myapp.models import *
from tastypie.exceptions import ImmediateHttpResponse
from tastypie import http
from auth import *
from code import *

class AccessTokenResource(ModelResource):
    """ Helps in generating a access token for a user based on role it has """
    class Meta:
        queryset = AccessToken.objects.all()
        resource_name = 'myauth/token'
        allowed_methods = ['get']
        fields = ["access_token"]
        authorization = Authorization()
        serializer = Serializer()


    def get_object_list(self, request):
        return super(AccessTokenResource, self).get_object_list(request)

    def dehydrate(self, bundle):
        user_id = bundle.request.GET['user']
        obj = User.objects.filter(pk__in=user_id)
        bundle.data['access_token'] = obj[0].user_access_id     ## we can encapsulate access_token with encode/decode -- look at code.py
        return bundle

class GroupResource(ModelResource):
    """ Rest based interface for /api/group """
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        fields = ['id', 'group_name', 'create_date']
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        serializer = Serializer()

class HotelResource(ModelResource):
    """ Rest based interface for /api/hotel """
    group_id = fields.ForeignKey(GroupResource, 'group')

    class Meta:
        queryset = Hotel.objects.all()
        resource_name = 'hotel'
        fields = ['id', 'hotel_name', 'hotel_city', 'hotel_region', 'create_date']
        allowed_methods = ['get', 'post']
        authorization = Authorization()
        serializer = Serializer()


class UserAccessResource(ModelResource):
    """ Rest based interface for /api/user_access/ """
    class Meta:
        queryset = UserAccess.objects.all()
        resource_name = 'user_access'
        authorization = Authorization()
        serializer = Serializer()


class UserResource(ModelResource):
    """ Rest based interface for /api/user """
    hotel_id = fields.ForeignKey(HotelResource, 'hotel')
    user_access_id = fields.ForeignKey(UserAccessResource, 'user_access')
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        authentication = Authentication()
        serializer = Serializer()



class RoomRatesResource(ModelResource):
    """ Rest based interface for /api/room_rates/ """
    class Meta:
        queryset = Room_Rates.objects.all()
        resource_name = 'room_rates'
        authentication = SillyAuthentication()      ## Custom authentication  -- auth.py
        authorization = SillyAuthorization()        ## Custom authorization   -- auth.py
        serializer = Serializer()

    def obj_get(self, request=None, **kwargs):
        raise ImmediateHttpResponse(response=http.HttpUnauthorized())