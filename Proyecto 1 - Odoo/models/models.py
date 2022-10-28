# -*- coding: utf-8 -*-

from odoo import models, fields, api #API SON LOS METADATOS @api.depends.

# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Aparcamiento(models.Model): #Herencia para heredar los metodos que se encuentran en Model.
    _name = "garage.Aparcamiento" #define al modelo real. #Si queremos buscar un aparcamiento se debe buscar por garaje.aparcamiento
    _description = "Permite definir las caracteristicas de un aparcamiento."
    name = fields.Char("Dirrecion", required=True) #Definimos el campo, descripcion o el texto que nos va ayudar a identificar al objeto cuando navegamos o cuando buscamos
    plazas = fields.Integer(string="Plazas", required=True) #required - true es un campo obligatorio.
    
    #-----------------------RELACION ENTRE TABLAS------------------------------------

    #RELACIONES ENTRE TABLAS: 

    # Es decir por un aparcamiento hay n de coches. ###Propiedades de navegacion###

    # la entidad padre tendriamos la coleccion del hijo, y del hijo la entidad padre.

    #Para comenzar vamos a crear una variable para almacenar una lista de coches. Para realizar esta accion se utiliza nombreDeClase_id. Y id si es una o ids si es mucha.

    Coche_ids = fields.One2many("garage.Coche", "Aparcamiento_Id", string="Coches")

    #PARA PODER DEFINIR LAS RELACIONES TENEMOS LOS DIFERENTES FIELDS:
    # UNO A MUCHOS [En este ejemplo seria un aparcamiento a muchos coches] -> One2many
    # MUCHO A UNO - > Many2one
    # MUCHOS A MUCHOS -> Many2many

    #Many significa muchos
    # 2 significa = a [two]
    # one significa uno


    #---------------------------------------------------------------------------------------------





class Coche(models.Model): 
    _name= "garage.Coche" #FORMATO DE TABLA PARA LAS RELACIONES.
    _description = "Permite definir las caracteristicas de los coches."
    _order ="name" #Permite indicar que orden por defecto va tener los datos de esta tabla.

    #-----------------------RELACION ENTRE TABLAS------------------------------------

    Aparcamiento_Id = fields.Many2one("garage.Aparcamiento", string="Aparcamiento") #Esto me sirve para decirle Odoo como vuelvo hacia atras. ##EL NOMBRE DEL PADRE##

    #RELACION ENTRE TABLAS:
    # -> En este caso muchos coches pueden estar vinculado a un solo garaje es decir MUCHOS A UNO.



    # ->  MANTENIMIENTO PUEDE TENER MUCHOS COCHES AL IGUAL QUE MANTEMIENTOS ENTONCES ESTO SERIA MUCHO A MUCHO.

    Mantenimiento_ids = fields.Many2many("garaje.Mantenimiento", string="Mantenimientos")

    #---------------------------------------------------------------------------------------------
    name = fields.Char(string="Matricula", required = True, size=7 ) #la matricula del coche
        #size: tamaño maximo de la matricula 7. No se va poner mas que  7 caracteres.

    descripcion = fields.Text("Descripcion")

    #¿Cual es la diferencia entre Text y Char? Que el text es para textos largos si tenemos campos cortos, como Direccion, nombre,ciudad, ect. Tenemos un Char. 

    modelo = fields.Char(string="Modelo", required = True) # el modelo del coche

    construido = fields.Date(string="Fecha de construccion")
        #.Date es fecha solamente / Datetime -> es fecha y hora.

    consumo = fields.Float("Consumo", (4,1), default= 0.0, help ="Consumo promedio de cada 100 kms") #() el valor float se define con una tupla. ES EL VALOR DE LA IZQUIERDA POR EL TOTAL DEL NUMERO (LA PRIMERA). Y LA SEGUNDA DECIMALES. En este caso decimos que el maximo consumo es de 4 digitos y un decimal.

    #default -> Me permite establecer un valor por defecto.

    # STORE = TRUE -> NO ES CONVENIENTE DE ESTE CASO.
    anual = fields.Integer("Años", compute="_get_anual")

    #compute -> este campo computado es campo especial donde no lo va meter el usuario, lo vamos a meter nosotros apartir de la fecha de construccion 

    @api.depends("construido") # ¿De que depende del año del coche? Depende construido -> Cuando el usuario cambie el año construido -> se va disparar automaticamente el metodo.
    def _get_anual(self):
        for coche in self:
            coche.anual = 0 #con el tode puede calcular la diferencia de año

class Mantenimiento(models.Model):

    _name = "garaje.Mantenimiento"
    _description = "Permite definir el mantenimiento rutinarios sobre conjuntos de coches."
    _order = "Fecha"
    #name = fields.Char()
    fecha = fields.Date("fecha", required = True, default = fields.date.today())
    # fields.date.today() -> Me devuelve la fecha de hoy.
    tipo = fields.Selection(string="Tipo", selection=[("l", "Lavar"), ("r", "Revision"), ("m", "Mecanica"), ("p", "Pintura")], default="l")
    #Para hacer una seleccion se debe hacer una lista de duplas.

    coste = fields.Float("Coste", (8,2), help ="Esto es el coste del mantenimiento total.")

    #Help -> permite darle algo descriptivo al usuario si se llega trabar.

    #-----------------------RELACION ENTRE TABLAS------------------------------------
    Coche_ids = fields.Many2many("garage.Coche", string="Mantenimiento")

    #CREARA UNA TABLA APARTE PARA QUE PODAMOS CONSULTAR DATOS SERIOS EN LA TABLA.

    #---------------------------------------------------------------------------


















#definimos una clase - hereda de models . Models