# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SportServiceCliente(models.Model):
    _name ='sportservice.cliente'
    _description = 'Creacion de cliente'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # models fields 
    name = fields.Char(
        string="Nombre",
        required = True,
    )
    birthDate = fields.Date(
        string="Fecha de nacimiento",
        default = fields.date.today(),
        required = True,
     )
     
    partnerId = fields.Integer(
        string="N° de cliente", 
        required = True,
    )
    
    serviceIds = fields.Many2many(
        comodel_name= 'sportservice.servicio',
        string="Servicios inscripto",
    )
    email = fields.Char(
        string="Correo electrónico",
        required = True,
        #compute = '_get_value_mail',
     )
    phone = fields.Char(
        string="Teléfono",
    )
    profilePicture = fields.Image(
        string="Imagen de perfil",
    )

    #@api.multi
    #@api.depends('email')

    #def _get_value_mail(self):
        #pass
