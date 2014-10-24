import re

def encode(param):
    """ Added encode method to encapsulate access_token that is created from user_id """
    return "access_xxx" + str(param + 1000)

def decode(param):
    """ Decode method for access_token """
    return int(param.split("access_xxx")[1])-1000