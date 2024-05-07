from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_sale_report_wizard(self):
        action = self.env.ref("ark_dev_training.action_sale_report_wizard").read()[0]
        return action
