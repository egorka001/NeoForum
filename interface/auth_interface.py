import sys
sys.path.append('../database/')
import base_auth

def check_valid(path, token, user):
    """go to base and look for user with token"""
    out = base_auth.base_check_valid(path, token, user)
    return out 

def update_base(path, token, login):
    out = base_auth.base_update(path, token, user)
    """go to base and add to login user"""
    return out
