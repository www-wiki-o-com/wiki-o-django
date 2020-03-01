"""  __      __    __               ___
    /  \    /  \__|  | _ __        /   \
    \   \/\/   /  |  |/ /  |  __  |  |  |
     \        /|  |    <|  | |__| |  |  |
      \__/\__/ |__|__|__\__|       \___/

A web service for sharing opinions and avoiding arguments

@file       core/management/command/clean.py
@copyright  GNU Public License, 2018
@authors    Frank Imeson
@brief      A managment script for cleaning up the database
"""


# *******************************************************************************
# Imports
# *******************************************************************************
from django.core.management.base import BaseCommand
from theories.models import Category


# *******************************************************************************
# Defines
# *******************************************************************************


# *******************************************************************************
# Methods
# *******************************************************************************


class Command(BaseCommand):
    """Runs a series of scripts to clean up the database."""
    help = __doc__

    def add_arguments(self, parser):
        # Optional arguments.
        parser.add_argument(
            '--categories',
            action='store_true',
            help='Remove empty cateogires.',
        )

    def handle(self, *args, **options):
        """The method that is run when the commandline is invoked."""

        # Clean up categories.
        if options['categories']:
            for category in Category.objects.all():
                if category.count() == 0:
                    category.delete()

        print("Done")