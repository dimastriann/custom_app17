# -*- coding: utf-8 -*-

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def write(self, vals):
        return super(ResPartner, self).write(vals)


class SaleOrder(models.Model):
    _inherit = "sale.order"
