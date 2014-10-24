from tastypie.utils.timezone import now
from django.db import models
from django.conf import settings

class AccessToken(models.Model):
    user_id = models.IntegerField(default=1)

class Group(models.Model):
    """ Represents a group of hotels like Taj """

    group_name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=now)
    is_billed = models.BooleanField(default=False)


class Hotel(models.Model):
    """ Represents one of the hotels like Taj Residency """
    group = models.ForeignKey('Group')
    hotel_name = models.CharField(max_length=200)
    hotel_city = models.CharField(max_length=200)
    hotel_region = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=now)
    pricing_plan = models.CharField(max_length=200, default='Basic')


class User(models.Model):
    """ Represents a user that is associated with Taj Residency """
    hotel = models.ForeignKey('Hotel')
    user_access = models.ForeignKey('UserAccess', null=True)    ## which type of user is this and what are the permissions
    user_first_name = models.CharField(max_length=200)
    user_last_name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=now)


class UserAccess(models.Model):
    """ Creates a relationship between user and role and role and its permissions
        1. user_type = designerrole, marketingrole
        2. user_access = 1,2, [decides permissions of that marketingrole/designerrole]
    """
    user_type = models.CharField(max_length=20, default='defaultrole')
    user_access = models.IntegerField(default=1)

##################################################################################

class Role(models.Model):
    """ Abstract Base Class to represent a Role """
    role_name = models.CharField(max_length=200)
    class Meta:
        abstract = True

class DefaultRole(models.Model):
    """ Sets a default role if role is not sure to be set """
    attribute_default = models.IntegerField(settings.GLOBAL_SETTINGS['NO_ACCESS'])

class MarketingRole(Role):
    """
        Represents a Marketing User for Taj. Now we have given default permissions to the user, but these can be changed
        We make this role scalable by creating different entries here that look like:
        1. Marketing Manager - room_rates:CRUD, promotions: CRUD, analytics: R, web_themes: No_ACCESS
        2. Marketing Executive - room_rates:R, promotions: CRUD, analytics: R, web_themes: No_ACCESS
    """
    room_rates = models.IntegerField(default=settings.GLOBAL_SETTINGS['CRUD_ACCESS'])
    promotions = models.IntegerField(default=settings.GLOBAL_SETTINGS['CRUD_ACCESS'])
    analytics = models.IntegerField(default=settings.GLOBAL_SETTINGS['READ_ACCESS'])
    web_themes = models.IntegerField(default=settings.GLOBAL_SETTINGS['NO_ACCESS'])

class DesignerRole(Role):
    """ Same as we have done for Marketing Role """
    analytics = models.IntegerField(default=settings.GLOBAL_SETTINGS['READ_ACCESS'])
    web_themes = models.IntegerField(default=settings.GLOBAL_SETTINGS['CRUD_ACCESS'])
    ux = models.IntegerField(default=settings.GLOBAL_SETTINGS['CRUD_ACCESS'])

class ResellerRole(Role):
    """ Same as we have done for Marketing Role """
    group = models.IntegerField(default=settings.GLOBAL_SETTINGS['NO_ACCESS'])
    hotel = models.IntegerField(default=settings.GLOBAL_SETTINGS['CRUD_ACCESS'])


##################################################################################

class Room(models.Model):
    """ Represents a Room """
    room_name = models.CharField(max_length=200)
    room_type = models.CharField(default='Basic',max_length=200)

class Room_Rates(models.Model):
    """ How can room rates be changed """
    room = models.ForeignKey('Room')
    isSeasonal = models.BooleanField(default=False)
    pricing = models.CharField(default='Basic', max_length=200)
    current_price = models.BigIntegerField()