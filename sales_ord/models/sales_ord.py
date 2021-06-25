# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Sale(models.Model):
    _inherit = 'sale.order'
    id_venta = fields.Char(default=False)
    latitud = fields.Char(default=False)
    longitud = fields.Char(default=False)
    arreglo = fields.Char(default=False)
    ruta =  fields.Many2one('account.analytic.account', string = 'Ruta', required = True)



