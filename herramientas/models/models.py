# -*- coding: utf-8 -*-

from odoo import models, fields, api

class herramientas_herramientas(models.Model):
     _name = 'herramientas.herramientas'
     _inherit = ['mail.thread', 'mail.activity.mixin']

     name = fields.Char(string="Nombre")
     tipo = fields.Char(string="Tipo")
     descripcion = fields.Text(string="Descripción")
     prod_id = fields.Many2one('mrp.production', string="Orden de producción")
     user = fields.Many2one('res.partner', string="Usuario asignado")
     tarea = fields.Many2one('project.task', string="Tarea asignada")

class Task(models.Model):
     _name = 'project.task'
     _inherit = 'project.task'

     herramientas = fields.One2many("herramientas.herramientas", "tarea", string = "Herramientas")

class herramientas_usuarios(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'

     herramientas = fields.One2many("herramientas.herramientas", "user", string = "Herramientas")

class herramientas_horas(models.Model):
     _name = 'herramientas.horas'

     horas = fields.Integer(string="Horas trabajadas")
     horas_extra = fields.Integer(string="Horas extra")
     tarea = fields.Many2one('project.task', string="Tarea trabajada")
     user = fields.Many2one('res.users', string="Nombre")

class horas_usuarios(models.Model):
     _name = 'res.users'
     _inherit = 'res.users'

     horas = fields.One2many("herramientas.horas", "user", string = "Horas")

class tareas_productos(models.Model):
     _name = 'project.task'
     _inherit = 'project.task'

     producto = fields.Many2many("product.template", string="Productos")

class tareas_facturas(models.Model):
     _name = 'project.task'
     _inherit = 'project.task'

     factura = fields.One2many("account.invoice", 'tarea', string="Factura")

class facturas_tareas(models.Model):
     _name = 'account.invoice'
     _inherit = 'account.invoice'

     tarea = fields.Many2one("project.task", string="Tarea")



     

