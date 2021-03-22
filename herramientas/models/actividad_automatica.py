# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class Task(models.Model):
#     _inherit = 'project.task'


#     @api.model
#     def write(self, values):
#         res = super(Task, self).create(values)

#         nuevo1 = self.env['account.invoice.line'].write({
#             'user_id': res.user_id.id,
#             'name' : res.name, 
#             'price_unit' : res.prace_unit ,
#             'quantity' : res.quantity,

#             })
            
#     return res
