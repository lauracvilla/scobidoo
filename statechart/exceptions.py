# Copyright 2016 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.exceptions import UserError


class NoTransitionError(UserError):
    pass
