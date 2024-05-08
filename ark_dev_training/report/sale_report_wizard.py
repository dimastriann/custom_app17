from odoo import fields, models


class SaleReportWizard(models.TransientModel):
    _name = "sale.report.wizard"
    _description = "Sale Report Wizard"

    start_date = fields.Date(default=fields.Date.today())
    end_date = fields.Date()
    sale_team_id = fields.Many2many("crm.team")

    def action_print_xlsx(self):
        sale = self.env["sale.order"].search(
            ['|',
             ("date_order", ">=", self.start_date),
             ("date_order", "<=", self.end_date)
             ]
        )
        return self.env.ref("ark_dev_training.action_report_training_excel").report_action(docids=sale)

    def action_print_pdf(self):
        sale = self.env["sale.order"].search(
            ['|',
                ("date_order", ">=", self.start_date),
                ("date_order", "<=", self.end_date)
            ]
        )
        return self.env.ref("sale.action_report_saleorder").report_action(docids=sale)
