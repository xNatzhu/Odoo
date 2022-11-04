# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models
from odoo.tools.translate import _
from dateutil.relativedelta import * 
from datetime import date 

class GarajeCoche(models.Model):
    _name = 'garaje.coche'
    _description = "garaje.coche"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order ='name'

    #model fields
    name = fields.Char(
        string = "Matricula",
        required = True,
        size = 7,
    )
    descripcion = fields.Text(
        string = "Descripcion",
    )
    modelo = fields.Char(
        string = "Modelo",
        required = True,
    )
    construido = fields.Date(
        string="Fecha del modelo",
    )
    consumo = fields.Float(
        string='Consumo', 
        default= 0.0, 
        help ='Consumo promedio de cada 100 kms'
    )
    averiado = fields.Boolean(
        string = "Averiado",
        default = False
    )
    
    #relational fields
    aparcamientoId = fields.Many2one(
        comodel_name='garaje.aparcamiento', 
        string='Aparcamiento'
    )
    mantenimientoIds = fields.Many2many(
        comodel_name='garaje.mantenimiento', 
        string='Mantenimiento'
    )

    # fields @api and compute

    anual = fields.Integer(
        string='Años', 
        compute='_get_anual'
    )

    @api.depends('construido')
    def _get_anual(self):
        for coche in self:
            fechaActual = date.today()
            coche.anual = relativedelta(
                fechaActual,
                coche.construido
            ).years
    
    #model constraint fields
    #Documentacion: https://www.odoo.com/documentation/15.0/es/developer/howtos/backend.html#model-constraints

    _sql_constraints = [('name_uniq','unique(name)', 'La matricula ya existe, porfavor ingresa otra.' )]
    