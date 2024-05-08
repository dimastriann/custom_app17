from odoo import api, fields, models


class ResDelegation(models.Model):
    _name = "res.delegation"
    _description = "Delegation Table"

    name = fields.Char()
    active = fields.Boolean(default=True)
    user_id = fields.Many2one(
        "res.users", string="Responsible", index=True,
        default=lambda self: self.env.user
    )
    description = fields.Text()
    value1 = fields.Float()
    value2 = fields.Float()
    total = fields.Float(compute="_compute_total_value", store=True)
    res_master_line = fields.One2many("res.master", "res_delegation_id")

    @api.depends("value1", "value2")
    def _compute_total_value(self):
        for rec in self:
            rec.total = rec.value1 * rec.value2


class ResMaster(models.Model):
    _name = "res.master"
    _description = "Res Master"
    _inherits = {"res.delegation": "res_delegation_id"}

    res_delegation_id = fields.Many2one(
        comodel_name="res.delegation", string="Res Delegation",
        ondelete="cascade", index=True, required=True,
    )
    value3 = fields.Float()
    total = fields.Float(compute="_compute_total_value", store=True)

    @api.depends("value3", "res_delegation_id.value1", "res_delegation_id.value2")
    def _compute_total_value(self):
        for rec in self:
            rec.total = rec.value1 * rec.value2 + rec.value3
