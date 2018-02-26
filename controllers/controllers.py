# -*- coding: utf-8 -*-
from odoo import http

# class Police(http.Controller):
#     @http.route('/police/police/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/police/police/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('police.listing', {
#             'root': '/police/police',
#             'objects': http.request.env['police.police'].search([]),
#         })

#     @http.route('/police/police/objects/<model("police.police"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('police.object', {
#             'object': obj
#         })