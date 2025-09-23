# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    char_mask = fields.Char(string="Character Mask", help="Example Character Mask")
    phone_mask = fields.Char(string="Phone Mask", help="Example Phone Mask")
