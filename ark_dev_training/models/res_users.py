from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    attendee_training_line = fields.One2many(
        "arkana.attendance.line", "attendee_id", string="Total Attendee"
    )


class ProductTemplate(models.Model):
    _inherit = "product.template"

    custom_price = fields.Float()
    list_price = fields.Float(string="Sales Price Inherit")

    def _set_barcode(self):
        # custom code
        res = super(ProductTemplate, self)._set_barcode()
        # custom code
        return res
