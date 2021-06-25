# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrder(models.Model):
#class Contacts(models.Model): # la clase debe tener un nombre significativo al modelo que vamos a modificar o heredar
    _inherit = 'res.partner'  #nombre del modelo que voy a heredar

    id_cliente = fields.Integer(default=False)    
    visita_lunes = fields.Boolean(default=False)
    visita_martes = fields.Boolean(default=False)
    visita_miercoles = fields.Boolean(default=False)
    visita_jueves = fields.Boolean(default=False)
    visita_viernes = fields.Boolean(default=False)
    visita_sabado = fields.Boolean(default=False)
    visita_domingo = fields.Boolean(default=False)
    cuenta_analitica = fields.Many2one('account.analytic.account', string = 'Cuenta Analitica')
    tipo_cliente = fields.Boolean(default=False)
    #comentario para reiniciar servicios
