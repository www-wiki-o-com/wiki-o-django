r""" __      __    __               ___
    /  \    /  \__|  | _ __        /   \
    \   \/\/   /  |  |/ /  |  __  |  |  |
     \        /|  |    <|  | |__| |  |  |
      \__/\__/ |__|__|__\__|       \___/

Copyright (C) 2018 Wiki-O, Frank Imeson

This source code is licensed under the GPL license found in the
LICENSE.md file in the root directory of this source tree.
"""

# *******************************************************************************
# Imports
# *******************************************************************************
from django.contrib import admin
from reversion.admin import VersionAdmin

from theories.models.categories import Category
from theories.models.opinions import Opinion, OpinionDependency
from theories.models.statistics import Stats, StatsDependency, StatsFlatDependency

# *******************************************************************************
# Classes
# *******************************************************************************


class CategoryAdmin(admin.ModelAdmin):
    pass


class OpinionAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        return ('user', 'theory')


class OpinionDependencyAdmin(admin.ModelAdmin):

    def get_user(self, obj):
        return obj.parent.user

    get_user.short_description = 'User'

    def get_list_display(self, request):
        return ('get_user', 'content')


class StatsAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        return ('stats_type', 'theory')


class StatsDependencyAdmin(admin.ModelAdmin):

    def get_owner(self, obj):
        return obj.parent.get_owner()

    get_owner.short_description = 'Type'

    def get_list_display(self, request):
        return ('get_owner', 'content')


class StatsFlatDependencyAdmin(admin.ModelAdmin):

    def get_owner(self, obj):
        return obj.parent.get_owner()

    get_owner.short_description = 'Type'

    def get_list_display(self, request):
        return ('get_owner', 'content')


# *******************************************************************************
# register
# *******************************************************************************
admin.site.register(Category, CategoryAdmin)
admin.site.register(Opinion, OpinionAdmin)
admin.site.register(OpinionDependency, OpinionDependencyAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(StatsDependency, StatsDependencyAdmin)
admin.site.register(StatsFlatDependency, StatsFlatDependencyAdmin)
