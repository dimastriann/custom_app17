# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.fields import Command


class ArkDevTraining(http.Controller):

    @http.route([
        "/v1/get_training",
        "/v1/get_training/<int:training_id>"], auth="none", type="json", methods=["GET"])
    def _get_data_training(self, training_id=False, *args, **kwargs):
        # custom code
        # process and return data GET
        domain = []
        if training_id:
            domain += [("id", "=", training_id)]

        data_training = request.env["arkana.training"]\
            .sudo()\
            .search(domain)\
            .read(["name", "responsible_id", "date_start", "date_end", "attendance_line"])
        return {"success": True, "code": 200, "result": data_training}

    @http.route("/v1/create_training", auth="user", type="json", methods=["POST"])
    def _create_data_training(self, *args, **kwargs):
        # custom code
        # process and return data POST
        data = request.httprequest.json
        for rec in data.get("values"):
            lines = rec.get("value_line")
            lines = [Command.create(vl) for vl in lines]
            rec.pop("value_line")
            rec["attendance_line"] = lines

        res = request.env["arkana.training"].create(data.get("values"))
        return {"result": {"success": True,"code": 200,"result": res.ids}}

    @http.route("/v1/update_training", auth="user", type="json", methods=["PUT"])
    def _update_data_training(self, *args, **kwargs):
        # custom code
        # process and return data UPDATE
        return {"result": {"success": True,"code": 200,"result": []}}

    @http.route("/v1/delete_training/<int:training_id>", auth="user", type="json", methods=["DELETE"])
    def _delete_data_training(self, training_id=False, *args, **kwargs):
        # custom code
        # process and return data DELETE
        res = request.env["arkana.training"].browse(training_id).unlink()
        return {"result": {"success": True,"code": 200,"result": res}}


#     @http.route('/ark_dev_training/ark_dev_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ark_dev_training/ark_dev_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ark_dev_training.listing', {
#             'root': '/ark_dev_training/ark_dev_training',
#             'objects': http.request.env['ark_dev_training.ark_dev_training'].search([]),
#         })

#     @http.route('/ark_dev_training/ark_dev_training/objects/<model("ark_dev_training.ark_dev_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ark_dev_training.object', {
#             'object': obj
#         })

