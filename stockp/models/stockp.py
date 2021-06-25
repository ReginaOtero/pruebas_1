# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Stockp(models.Model):
#class Contacts(models.Model): # la clase debe tener un nombre significativo al modelo que vamos a modificar o heredar
    _inherit = 'stock.picking'  #nombre del modelo que voy a heredar

    previo = fields.Boolean(default=False)
    ruta = fields.Integer(default=False)
    liquidado = fields.Boolean(default=False)
    tipo_cliente = fields.Boolean(default=False)
    sup_de_ruta = fields.Many2one('res.users', string = 'Supervisor', required = False)





