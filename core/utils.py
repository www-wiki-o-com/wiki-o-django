"""      __      __    __                  __
        /  \    /  \__|  | _ __           /   \
        \   \/\/   /  |  |/ /  |  ______ |  |  |
         \        /|  |    <|  | /_____/ |  |  |
          \__/\__/ |__|__|__\__|          \___/

A web service for sharing opinions and avoiding arguments

@file       core/utils.py
@brief      A collection of utility methods/classes
@details
@copyright  GNU Public License, 2018
@authors    Frank Imeson
"""


# *******************************************************************************
# Imports
# *******************************************************************************
import re
import enum

from actstream import action
from actstream.models import Action
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from notifications.signals import notify


# *******************************************************************************
# Defines
# *******************************************************************************
DEBUG = False


class LogDiffResult(enum.Enum):
    """Enum for log_is_different return result."""
    MATCH = 1
    DIFFERENT = 2
    UPDATED = 3


# *******************************************************************************
# Methods
# *******************************************************************************


def get_or_none(objects, **kwargs):
    """Queries a data model for a matching object.

    Example: get_or_none(theory.opinions, user=current_user)

    Args:
        objects (QuerySet): A reference to the model's objects.

    Returns:
        Object or None: The unique matching object, None otherwise.
    """    
    try:
        return objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None


def get_first_or_none(objects, **kwargs):
    """Queries a data model for the first matching object.

    Args:
        objects (QuerySet): A reference to the model's objects.

    Returns:
        Object or None: The unique matching object, None otherwise.
    """
    try:
        return objects.filter(**kwargs).first()
    except ObjectDoesNotExist:
        return None


def stream_if_unique(target_actions, log, accept_time=21600):
    """Checks if the input log(s) contents are different than the input parameters.

    Example: stream_if_unique(self.targets, log={'sender':self.user, 'verb':'Bob creates a theory'})

    Args:
        target_actions (Actions or Steam): The set of logs to compare against.
        log (dict): A dict with the relevent log info ('sender', 'verb', 'action_object', 'target').
        accept_time (int, optional): The age in seconds that the log must be to be valid.
            Defaults to 21600.

    Returns:
        bool: True if updated, false otherwise.
    """
    assert isinstance(log, dict)
    last_action = target_actions.first()
    result = log_is_different(last_action, log, accept_time=accept_time)
    if result == LogDiffResult.DIFFERENT:
        kwargs = log.copy()
        del kwargs['sender']
        action.send(log['sender'], **kwargs)
        return True
    return False


def notify_if_unique(follower, log, update_unread=True, accept_time=21600):
    """Checks if the input log(s) contents are different than the input parameters.

    Example: notify_if_unique(follower, log={'sender':self.user, "Bob farts", self.theory})

    Args:
        follower (User): The user following the object.
        log (dict): A dict with the relevent log info ('sender', 'verb', 'action_object', 'target').
        update_unread (bool, optional): If enabled read messages are updated to unread.
            Defaults to True.
        accept_time (int, optional): The age in seconds that the log must be to be valid.
            Defaults to 21600.

    Returns:
        bool: True if the user has ben notified, false otherwise.
    """
    assert isinstance(log, dict)
    last_notification = follower.notifications.first()
    result = log_is_different(last_notification, log, update_unread, accept_time)
    if result == LogDiffResult.DIFFERENT:
        notify.send(**log)
        return True
    return False


def log_is_different(old_log, new_log, update_unread=False, accept_time=21600):
    """Checks if the input log's contents are different than the input parameters.

    Example: log_is_different(old_log, new_log={'sender':self.user, 'verb':'Bob farts'})

    Args:
        old_log (Log): The exsiting log to compare against.
        new_log (dict): The new log.
        update_unread (bool, optional): If the old log has been read and the new log is different,
            change it to unread. Defaults to False. May contain the following keys:
                sender: The user/object responsible for the action.
                verb: The phrase that identifies the action.
                action_object: The object linked to the action.
                target: The object to which the action was performed.
        accept_time (int, optional): The age in seconds that the log must be to be valid.
            Defaults to 21600.

    Returns:
        LogDiffResult: May return DIFFERENT, MATCHED, or UPDATED.
    """
    # Preconditions
    assert isinstance(new_log, dict)

    # Test if log is different
    if old_log is None:
        return LogDiffResult.DIFFERENT
    if old_log.actor != new_log.get('sender'):
        return LogDiffResult.DIFFERENT
    if old_log.verb != new_log.get('verb'):
        return LogDiffResult.DIFFERENT
    if old_log.action_object != new_log.get('action_object'):
        return LogDiffResult.DIFFERENT
    if old_log.target != new_log.get('target'):
        return LogDiffResult.DIFFERENT

    # The log matches but it's too old
    elapsed_time = timezone.now() - old_log.timestamp
    if elapsed_time.total_seconds() >= accept_time:
        return LogDiffResult.DIFFERENT

    # The log matches but it's read, mark it back to unread
    if update_unread and isinstance(old_log, Action) and old_log.read():
        old_log.mark_as_unread()
        return LogDiffResult.UPDATED

    # The log matches
    return LogDiffResult.MATCH


def get_form_data(response, verbose_level=0):
    """A helper method for parsing form data from a post response.

    Args:
        response (dict): The post respose.
        verbose_level (int, optional): The verbose level used for debugging. Defaults to 0.

    Returns:
        data: A more consise set of form data.
    """
    # Preconditions
    if response.context is None or not hasattr(response.context, 'keys'):
        return None

    # Setup
    data = {}
    for content_name in response.context.keys():
        # Parse a formsets
        if re.search(r'formset', content_name):
            formset = response.context[content_name]

            # Parse the formset managmenet data
            form = formset.management_form
            for field in form.fields.keys():
                data['%s-%s' % (form.prefix, field)] = form[field].value()

            # Parse each set of form data
            for form in formset.forms:
                for field in form.fields.keys():
                    if form[field].value() is None:
                        data['%s-%s' % (form.prefix, field)] = ''
                    else:
                        data['%s-%s' % (form.prefix, field)] = form[field].value()

        # Parse a single form
        elif re.search(r'form', content_name):
            form = response.context[content_name]
            if not isinstance(form, bool):
                for field in form.fields.keys():
                    if form.prefix is None:
                        data['%s' % (field)] = form[field].value()
                    else:
                        data['%s-%s' % (form.prefix, field)] = form[field].value()

    # Print debug info
    if verbose_level >= 10:
        for x in data:
            print("get_form_data:", x, data[x])

    # Return result
    return data


# *******************************************************************************
# Classes
# *******************************************************************************


class QuerySetDict():
    """A class for converting query sets into dicts."""

    def __init__(self, attrib_key, queryset=None):
        self.dict = {}
        self.attrib_key = attrib_key
        if queryset is not None:
            for x in queryset:
                self.dict[self.get_key(x)] = x

    def __iter__(self):
        self.dict_iter = self.dict.values().__iter__()
        return self

    def __next__(self):
        return self.dict_iter.__next__()

    def __str__(self):
        return str(list(self))

    def get_key(self, obj):
        key = obj
        for key_str in self.attrib_key.split('.'):
            key = getattr(key, key_str)
        return key

    def add(self, x):
        self.dict[self.get_key(x)] = x

    def get(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return None

    def count(self):
        return len(self.dict)