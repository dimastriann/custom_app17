# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ArkanaTraining(models.Model):
    _name = "arkana.training"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Arkana Training"

    # === Basic Fields === #
    name = fields.Char(default="New")
    value = fields.Integer()
    active = fields.Boolean(default=True)

    # === Advanced Fields === #

    attachment = fields.Binary(attachment=False)
    filename = fields.Char()
    # image = fields.Image(max_width=200, max_height=200)
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("cancel", "Canceled"),
        ],
        default="draft",
        string="Status",
        readonly=True,
        required=True,
        tracking=True,
    )
    is_paid = fields.Boolean()
    note = fields.Text(translate=True)
    total = fields.Integer()
    total_attendee = fields.Integer(
        compute="_compute_total", inverse="_inverse_total", store=True, readonly=True
    )
    responsible_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        domain=[("create_employee_id", "!=", False)],
        ondelete="cascade",
    )
    trainer_ids = fields.Many2many(
        comodel_name="res.users",
        column1="ark_training_id",
        column2="user_id",
        relation="arkana_training_res_user_rel",
        string="Trainer's",
    )
    attendance_line = fields.One2many(
        comodel_name="arkana.attendance.line", inverse_name="arkana_training_id"
    )
    price = fields.Monetary(currency_field="currency_id")

    # date = fields.Date()
    date_start = fields.Datetime(string="Date Start")
    date_end = fields.Datetime(string="Date End")
    # html = fields.Html()

    @api.depends("attendance_line")
    def _compute_total(self):
        for rec in self:
            # self.env.context
            rec.total_attendee = len(rec.attendance_line)

    def _inverse_total(self):
        for rec in self:
            rec.total = rec.total_attendee

    currency_id = fields.Many2one("res.currency")
    company_id = fields.Many2one("res.company")

    # === Automatic Fields === #
    # log access #
    # id, create_uid, create_date, write_uid, write_date

    # === Reserved Fields === #

    @api.model_create_multi
    def create(self, vals_list):
        # custom code
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("arkana.training")
        res = super(ArkanaTraining, self).create(vals_list)
        # custom code
        return res

    def read(self, fields=None, load="_classic_read"):
        return super(ArkanaTraining, self).read(fields, load)

    def write(self, vals):
        res = super(ArkanaTraining, self).write(vals)
        for rec in self:
            pass
        return res

    def unlink(self):
        # custom code
        for rec in self:
            pass
        return super(ArkanaTraining, self).unlink()

    # @api.ondelete(at_uninstall=False)
    # def _check_unlink_data(self):
    #     for rec in self:
    #         pass

    def action_approve(self):
        self.write({"state": "approved"})

    def action_cancel(self):
        self.write({"state": "cancel"})

    def _get_data_from_query(self):
        # so_orm = self.env["sale.order"].browse([7])
        self.env.cr.execute("select * from sale_order where id = 7")
        data = self.env.cr.dictfetchone()
        return data

    def action_test_json_rpc(self):
        pass

    def action_test_xml_rpc(self):
        pass


class AttendanceLine(models.Model):
    _name = "arkana.attendance.line"
    _description = "Attendance Training"

    name = fields.Char()
    arkana_training_id = fields.Many2one(
        comodel_name="arkana.training",
        required=True,
        string="Arkana Training",
        ondelete="cascade",
    )
    attendee_id = fields.Many2one(
        comodel_name="res.users", string="Attendee", required=True, ondelete="restrict"
    )
    payment_state = fields.Selection(
        selection=[
            ("free", "Free"),
            ("no_payment", "No Payment"),
            ("payment", "Payment"),
        ],
        string="Payment Status",
        required=True,
        default="free",
        compute="_compute_payment_state",
        store=True,
    )

    @api.depends("arkana_training_id.is_paid")
    def _compute_payment_state(self):
        for line in self:
            line.payment_state = line.payment_state
