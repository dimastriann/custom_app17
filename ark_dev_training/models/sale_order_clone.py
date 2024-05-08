from odoo import api, fields, models


class SaleOrderClone(models.Model):
    _name = "sale.order.clone"
    _inherit = ["sale.order"]
    _description = "Sale Order Clone"

    transaction_ids = fields.Many2many(
        comodel_name='payment.transaction',
        relation='sale_order_clone_transaction_rel',
        column1='sale_order_clone_id',
        column2='transaction_id',
        string="Transactions",
        copy=False, readonly=True
    )
    tag_ids = fields.Many2many(
        comodel_name='crm.tag',
        relation='sale_order_clone_tag_rel',
        column1='order_clone_id',
        column2='tag_id',
        string="Tags"
    )

    # order_clone_line = fields.One2many(
    #     comodel_name='sale.order.line',
    #     inverse_name='order_clone_id',
    #     string="Order Lines",
    #     copy=True, auto_join=True)



# class SaleOrderLine(models.Model):
#     _inherit = "sale.order.line"
#
#     order_clone_id = fields.Many2one("sale.order.clone", string="SO Clone")