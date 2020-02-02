"""  __      __    __               ___
    /  \    /  \__|  | _ __        /   \
    \   \/\/   /  |  |/ /  |  __  |  |  |
     \        /|  |    <|  | |__| |  |  |
      \__/\__/ |__|__|__\__|       \___/

A web service for sharing opinions and avoiding arguments

@file       theories/tests/views01.py
@brief      A collection of unit tests for the app's views with a specific set of user permissions
@copyright  GNU Public License, 2018
@authors    Frank Imeson
"""


# *******************************************************************************
# imports
# *******************************************************************************
from . views00 import *


# ************************************************************
# Anonymous user tests with data created by bob
#
#
#
#
#
# ************************************************************
class AnonymousUserViews(TestCase, ViewsTestBase):
    fixtures = ['groups.json']

    # ******************************
    # Setup - AnonymousUser
    # ******************************
    def setUp(self):
        super().create_data()

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_index(self):
        super().test_get_index(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_index_category(self):
        super().test_get_index_category(
            override=True,
            category='legal',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_activity(self):
        super().test_get_activity(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_create(self):
        super().test_get_theory_create(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_detail(self):
        super().test_get_theory_detail(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_edit(self):
        super().test_get_theory_edit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_merge(self):
        super().test_get_theory_merge(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_backup(self):
        super().test_get_theory_backup(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_restore(self):
        super().test_get_theory_restore(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_activity(self):
        super().test_get_theory_activity(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_edit_evidence(self):
        super().test_get_theory_edit_evidence(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_edit_subtheories(self):
        super().test_get_theory_edit_subtheories(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_theory_inherit(self):
        super().test_get_theory_inherit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_evidence_detail(self):
        super().test_get_evidence_detail(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_evidence_edit(self):
        super().test_get_evidence_edit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_evidence_merge(self):
        super().test_get_evidence_merge(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_evidence_restore(self):
        super().test_get_evidence_restore(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_evidence_activity(self):
        super().test_get_evidence_activity(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_opinion_demo(self):
        super().test_get_opinion_demo(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_opinion_detail(self):
        super().test_get_opinion_detail(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_my_opinion(self):
        super().test_get_my_opinion(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_opinion_edit(self):
        super().test_get_opinion_edit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_opinion_slug(self):
        super().test_get_opinion_slug(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_user_vs_user(self):
        super().test_get_user_vs_user(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_user_vs_slug(self):
        super().test_get_user_vs_slug(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_slug_vs_user(self):
        super().test_get_slug_vs_user(
            override=True,
        )

    # ******************************
    # GET - AnonymousUser
    # ******************************
    def test_get_slug_vs_slug(self):
        super().test_get_slug_vs_slug(
            override=True,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_create(self):
        super().test_post_theory_create(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            created=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_edit(self):
        super().test_post_theory_edit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_merge(self):
        super().test_post_theory_merge(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_backup(self):
        super().test_post_theory_backup(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_delete_backup(self):
        super().test_post_theory_delete_backup(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_edit_evidence(self):
        super().test_post_theory_edit_evidence(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_edit_subtheories(self):
        super().test_post_theory_edit_subtheories(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_new_evidence(self):
        super().test_post_theory_new_evidence(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            created=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_new_subtheories(self):
        super().test_post_theory_new_subtheories(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            created=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_inherit(self):
        super().test_post_theory_inherit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_delete(self):
        super().test_post_theory_delete(
            override=True,
            code=403,
            deleted=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_convert01(self):
        super().test_post_theory_convert01(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_convert02(self):
        super().test_post_theory_convert02(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_revert(self):
        super().test_post_theory_revert(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_add_to_home(self):
        super().test_post_theory_add_to_home(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_theory_remove_from_home(self):
        super().test_post_theory_remove_from_home(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_edit(self):
        super().test_post_evidence_edit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_merge(self):
        super().test_post_evidence_merge(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_delete_backup(self):
        super().test_post_evidence_delete_backup(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_delete(self):
        super().test_post_evidence_delete(
            override=True,
            code=403,
            deleted=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_backup(self):
        super().test_post_evidence_backup(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_convert(self):
        super().test_post_evidence_convert(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_evidence_revert(self):
        super().test_post_evidence_revert(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - Level04User
    # ******************************
    def test_post_opinion_new(self):
        super().test_post_opinion_new(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_opinion_edit(self):
        super().test_post_opinion_edit(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_delete_my_opinion(self):
        super().test_post_delete_my_opinion(
            override=True,
            code=403,
            deleted=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_delete_bobs_opinion(self):
        super().test_post_delete_bobs_opinion(
            override=True,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_opinion_copy(self):
        super().test_post_opinion_copy(
            override=True,
            code=302,
            redirect_url='/accounts/login/',
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_hide_my_opinion(self):
        super().test_post_hide_my_opinion(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_hide_bobs_opinion(self):
        super().test_post_hide_bobs_opinion(
            override=True,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_reveal_my_opinion(self):
        super().test_post_reveal_my_opinion(
            override=True,
            code=403,
            modified=False,
        )

    # ******************************
    # POST - AnonymousUser
    # ******************************
    def test_post_reveal_bobs_opinion(self):
        super().test_post_reveal_bobs_opinion(
            override=True,
        )