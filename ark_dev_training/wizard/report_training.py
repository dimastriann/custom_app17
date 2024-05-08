from odoo import api, fields, models


class ReportTraining(models.TransientModel):
    _name = "report.training.wizard"
    _description = "Report Training Wizard"

    training_id = fields.Many2one(
        comodel_name="arkana.training", string="Arkana Training",
        default=lambda self: self.env.context.get("active_id")
    )
    start_date = fields.Date