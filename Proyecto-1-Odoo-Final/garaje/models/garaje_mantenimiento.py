# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models
from odoo.tools.translate import _


class GarajeMantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = "garaje.mantenimiento"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'fecha'
    #model field
    fecha = fields.Date(
        string = "Fecha",
        required = True,
        default = fields.date.today()
    )
    tipo = fields.Selection(
        string = "Tipo",
        required = True,
        selection = [
            ('l', 'Lavado'), 
            ('r', 'Revision'), 
            ('p', 'Pintura'), 
            ('m', 'Mecanica')], 
            default = 'l'
    )

    coste = fields.Float(
        'Costo de mantenimiento',
        (5,4),
        required = True
    )

    

    
