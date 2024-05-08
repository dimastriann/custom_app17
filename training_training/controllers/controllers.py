# -*- coding: utf-8 -*-
# from odoo import http


# class TrainingTraining(http.Controller):
#     @http.route('/training_training/training_training', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/training_training/training_training/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('training_training.listing', {
#             'root': '/training_training/training_training',
#             'objects': http.request.env['training_training.training_training'].search([]),
#         })

#     @http.route('/training_training/training_training/objects/<model("training_training.training_training"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('training_training.object', {
#             'object': obj
#         })

