"""  __      __    __               ___
    /  \    /  \__|  | _ __        /   \
    \   \/\/   /  |  |/ /  |  __  |  |  |
     \        /|  |    <|  | |__| |  |  |
      \__/\__/ |__|__|__\__|       \___/

A web service for sharing opinions and avoiding arguments

@file       users/utils.py
@brief      A collection of app specific utility methods/classes
@copyright  GNU Public License, 2018
@authors    Frank Imeson
"""


# *******************************************************************************
# Imports
# *******************************************************************************
import logging
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from users.models import User


# *******************************************************************************
# Defines
# *******************************************************************************
LOGGER = logging.getLogger(__name__)


# *******************************************************************************
# Methods
# *******************************************************************************


# stackoverflow.com/questions/22250352/programmatically-create-a-django-group-with-permissions
def create_groups_and_permissions():
    """
    Create the set of groups and permissions used by Wiki-O. This method
    is used for unit tests and the initial setup of Wiki-O's DB.
    """
    group, created = Group.objects.get_or_create(name='user level: 0')
    for x in ['change', 'add', 'delete']:
        for y in ['opinion']:
            name = '%s_%s' % (x, y)
            content_type = ContentType.objects.get(app_label='theories', model=y)
            perm, created = Permission.objects.get_or_create(
                content_type=content_type, codename=name)
            group.permissions.add(perm)
            if created:
                LOGGER.info('Created %s permissions.', perm)
    for level in range(1, 5):
        group, created = Group.objects.get_or_create(
            name='user level: %d' % level)
        for x in ['change', 'add', 'delete', 'view']:
            for y in ['category', 'theorynode', 'opinion']:
                name = '%s_%s' % (x, y)
                content_type = ContentType.objects.get(app_label='theories', model=y)
                perm, created = Permission.objects.get_or_create(
                    content_type=content_type, codename=name)
                group.permissions.add(perm)
                if created:
                    LOGGER.info('Created %s permissions.', perm)
    LOGGER.info('Created default group and permissions.')


def create_test_user(username='bob', password='1234', level=None):
    """
    Create a test user.

    @details    Primarly used for unit tests.
    @param[in]  username (optional, default bob): The user's name.
    @param[in]  password (optional, default 1234): The user's password.
    @param[in]  level (optional, default None): The user's permission level.
    """
    user = User.objects.create_user(
        username=username,
        password=password,
    )
    if level is not None:
        if level == 0:
            user.demote(new_level=level)
        if level >= 1:
            user.promote(new_level=level)
    return user
