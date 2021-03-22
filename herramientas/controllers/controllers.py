# -*- coding: utf-8 -*-
from odoo import http

# class Herramientas(http.Controller):
#     @http.route('/herramientas/herramientas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/herramientas/herramientas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('herramientas.listing', {
#             'root': '/herramientas/herramientas',
#             'objects': http.request.env['herramientas.herramientas'].search([]),
#         })

#     @http.route('/herramientas/herramientas/objects/<model("herramientas.herramientas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('herramientas.object', {
#             'object': obj
#         })