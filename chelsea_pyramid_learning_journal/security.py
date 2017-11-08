"""Security and login info."""

import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Everyone, Authenticated
from pyramid.security import Allow
from passlib.apps import custom_app_context as pwd_context


def is_authorized(user, password):
    """Check if the user's username and password are good."""
    if user == os.environ.get('AUTH_USERNAME', ''):
        if pwd_context.verify(password, os.environ.get('AUTH_PASSWORD', 'weeeee')):
            return True
    return False


class MyRoot(object):
    """Root security access."""

    def __init__(self, request):
        """Init security settings."""
        self.request = request

    __acl__ = [
        # (Allow, Everyone, 'view'),
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'secret'),
    ]


def includeme(config):
    """Security-related configuration."""
    auth_secret = os.environ.get('AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )
    config.set_authentication_policy(authn_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(MyRoot)
