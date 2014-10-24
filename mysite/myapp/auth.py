from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.exceptions import Unauthorized
from models import *
from django.db.models.loading import get_model



def getRoleDBObj(access_token):
    """
        Based on access_token, we know the user is of which
        1. type designer role, marketing role etc and
        2. access_id tells us what list of permissions are set for this designer/marketeer
        During runtime we create the object of the role DB that needs to look up for permissions
    """
    uaObj = UserAccess.objects.filter(pk__in=access_token)
    role, access_id = uaObj[0].user_type, uaObj[0].user_access

    #During runtime we create the object of the role DB that needs to look up for permissions
    roleDB = get_model(app_label='myapp', model_name=str(role))

    #Exact row where permissions exist
    roleObj = roleDB.objects.filter(pk__in=access_id)

    return roleObj

################################ AUTHORIZATION ################################

class SillyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        access_token = bundle.request.GET["access_token"]
        roleObj = getRoleDBObj(access_token)

        if roleObj[0].room_rates == settings.GLOBAL_SETTINGS['READ_ACCESS']:
            return object_list
        else:
            raise Unauthorized("Sorry, no reads.")


    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.user == bundle.request.user

    def create_list(self, object_list, bundle):
        access_token = bundle.request.GET["access_token"]
        roleObj = getRoleDBObj(access_token)
        if roleObj[0].room_rates == settings.GLOBAL_SETTINGS['CRUD_ACCESS']:
            return object_list
        else:
            raise Unauthorized("Sorry, no writes.")

    def create_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


################################ AUTHENTICATION ################################

class SillyAuthentication(Authentication):
    def is_authentication(self, request, **kwargs):
        if request.GET['access_token']:
          print True
          return True

        print False
        return False

    # Optional but recommended
    def get_identifier(self, request):
        return request.user.username