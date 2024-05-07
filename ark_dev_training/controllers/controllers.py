# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ArkDevTraining(http.Controller):

    @http.route([
        "/v1/get_training",
        "/v1/get_training/<int:training_id>"], auth="none", type="json", methods=["GET"])
    def _get_data_training(self, training_id=False, *args, **kwargs):
        # custom code
        # process and return data GET
        data_training = request.env["arkana.training"]\
            .sudo()\
            .search([])\
            .read(["name", "responsible_id", "date_start", "date_end", "attendance_line"])
        return {"success": True, "code": 200, "result": data_training}

    @http.route("/v1/create_training", auth="user", type="json", methods=["POST"])
    def _create_data_training(self, *args, **kwargs):
        # custom code
        # process and return data POST
        return {"result": {"success": True,"code": 200,"result": []}}

    @http.route("/v1/update_training", auth="user", type="json", methods=["PUT"])
    def _update_data_training(self, *args, **kwargs):
        # custom code
        # process and return data UPDATE
        return {"result": {"success": True,"code": 200,"result": []}}

    @http.route("/v1/delete_training/<int:training_id>", auth="none", type="json", methods=["DELETE"])
    def _delete_data_training(self, training_id=False, *args, **kwargs):
        # custom code
        # process and return data DELETE
        return {"result": {"success": True,"code": 200,"result": []}}


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

