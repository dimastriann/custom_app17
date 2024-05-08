from odoo import models


class TrainingReport(models.AbstractModel):
    _name = "report.ark_dev_training.training_report"
    _inherit = "report.report_xlsx.abstract"
    _description = "Training Report"

    def generate_xlsx_report(self, workbook, data, objs):
        for obj in objs:
            report_name = obj.name
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)
