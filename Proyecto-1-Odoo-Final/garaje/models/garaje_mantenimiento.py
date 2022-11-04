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
            ('m', 'Mecanica')
        ],
        default = 'l'
    )

    coste = fields.Float(
        string='Costo de mantenimiento',
        required = True
    )

    #relational fields
    cocheIds = fields.Many2many(
        comodel_name='garaje.coche', 
        string='Coches'
    )

    #ORN API 

    def name_get(self):
        resultados = []
        for mantenimiento in self:
            descripcion = f'{len(mantenimiento.cocheIds)} coches - gastos: {mantenimiento.coste} $'
            resultados.append((mantenimiento.id, descripcion))
                               #id element       #text
        return resultados

        # Documentacion: https://www.odoo.com/documentation/15.0/es/developer/reference/backend/orm.html#record-set-information

    
