# -*- coding: utf-8 -*-
# from odoo import http


# class ArkanaTest(http.Controller):
#     @http.route('/arkana_test/arkana_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arkana_test/arkana_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arkana_test.listing', {
#             'root': '/arkana_test/arkana_test',
#             'objects': http.request.env['arkana_test.arkana_test'].search([]),
#         })

#     @http.route('/arkana_test/arkana_test/objects/<model("arkana_test.arkana_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arkana_test.object', {
#             'object': obj
#         })

