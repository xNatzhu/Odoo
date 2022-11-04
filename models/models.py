# -*- coding: utf-8 -*-

from odoo import models, fields, api #API SON LOS METADATOS @api.depends.
from dateutil.relativedelta import * #Y este nos permite saber la diferencia entre dos fechas.
from datetime import date #Nos va brindar la fecha actual en este import

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
    _name = 'garaje.Aparcamiento' #define al modelo real. #Si queremos buscar un aparcamiento se debe buscar por garaje.aparcamiento. ESTE NOMBRE ES EL NOMBRE DEL OBJETO ES DECIR SERA LO QUE LO VA IDENTIFICAR.

    _description = 'Permite definir las caracteristicas de un aparcamiento.' 
    name = fields.Char('Dirrecion', required=True) #Definimos el campo, descripcion o el texto que nos va ayudar a identificar al objeto cuando navegamos o cuando buscamos
    plazas = fields.Integer(string='Plazas', required=True) #required - true es un campo obligatorio.
    
    #-----------------------RELACION ENTRE TABLAS------------------------------------

    #RELACIONES ENTRE TABLAS: 

    # Es decir por un aparcamiento hay n de coches. ###Propiedades de navegacion###

    # la entidad padre tendriamos la coleccion del hijo, y del hijo la entidad padre.

    #Para comenzar vamos a crear una variable para almacenar una lista de coches. Para realizar esta accion se utiliza nombreDeClase_id. Y id si es una o ids si es mucha.

    Coche_ids = fields.One2many('garaje.Coche', 'Aparcamiento_Id', string='Coches') #NO AGREGARLO POR EL MOMENTO.

    #PARA PODER DEFINIR LAS RELACIONES TENEMOS LOS DIFERENTES FIELDS:
    # UNO A MUCHOS [En este ejemplo seria un aparcamiento a muchos coches] -> One2many
    # MUCHO A UNO - > Many2one
    # MUCHOS A MUCHOS -> Many2many

    #Many significa muchos
    # 2 significa = a [two]
    # one significa uno

    #EXPLICacion de logica del funcionamiento de los campos relacionales.

    # 1. El many2one lo que te permite es brindarte muchas opciones pero puedes escoger una. Ejemplo Ciudad tendras varias ciudades pero puedes escoger una. Funciona como un selecccion. Lleva como parametro el modelo que sera el campo relacional
    #Otro ejemplo: Si tuvieramos una clase llamada coche y tenemos que llevarlo a un aparcamiento. Los coches van ser muchos pero solamente va existir un solo aparcamiento donde se va guardar.

    # 2.  El one2many basicamente es un solo elemento que contienes PERO tendras una serie de campos que podras rellenarlo, es decir tendras un elemento que ocupara x cantidades de columnas. Es decir podremos elegir solamente UNO pero tendremos muchos campos para rellenar. Seria estilo formulario.

    # 3. many2many -> Es una combinacion de ambos. Con la diferencia que el One2Many tenias que elegir una opcion aca directamente puedes seleccionar varios elementos y temdras varias columnas.

    #Ejemplo: Puedo seleccionar 10 chicos para que vayan a diferentes clases.
    #---------------------------------------------------------------------------------------------





class Coche(models.Model): 
    _name= 'garaje.Coche' #FORMATO DE TABLA PARA LAS RELACIONES.
    _description = 'Permite definir las caracteristicas de los coches.'
    _order ='name' #Permite indicar que orden por defecto va tener los datos de esta tabla.

    #-----------------------RELACION ENTRE TABLAS------------------------------------

    Aparcamiento_Id = fields.Many2one('garaje.Aparcamiento', string='Aparcamiento') #Esto me sirve para decirle Odoo como vuelvo hacia atras. ##EL NOMBRE DEL PADRE##

    #RELACION ENTRE TABLAS:
    # -> En este caso muchos coches pueden estar vinculado a un solo garaje es decir MUCHOS A UNO.



    # ->  MANTENIMIENTO PUEDE TENER MUCHOS COCHES AL IGUAL QUE MANTEMIENTOS ENTONCES ESTO SERIA MUCHO A MUCHO.

    Mantenimiento_ids = fields.Many2many('garaje.Mantenimiento', string='Mantenimientos')

    #---------------------------------------------------------------------------------------------
    name = fields.Char(string='Matricula', required = True, size=7 ) #la matricula del coche
        #size: tamaño maximo de la matricula 7. No se va poner mas que  7 caracteres.

    descripcion = fields.Text('Descripcion')

    #¿Cual es la diferencia entre Text y Char? Que el text es para textos largos si tenemos campos cortos, como Direccion, nombre,ciudad, ect. Tenemos un Char. 

    modelo = fields.Char(string='Modelo', required = True) # el modelo del coche

    construido = fields.Date(string='Fecha de construccion')
        #.Date es fecha solamente / Datetime -> es fecha y hora.

    consumo = fields.Float('Consumo', (4,1), default= 0.0, help ='Consumo promedio de cada 100 kms') #() el valor float se define con una tupla. ES EL VALOR DE LA IZQUIERDA POR EL TOTAL DEL NUMERO (LA PRIMERA). Y LA SEGUNDA DECIMALES. En este caso decimos que el maximo consumo es de 4 digitos y un decimal.

    #default -> Me permite establecer un valor por defecto.

    averiado = fields.Boolean(string="Averiado", default= False) #Campo boleano.
    # STORE = TRUE -> NO ES CONVENIENTE DE ESTE CASO.
    anual = fields.Integer('Años', compute='_get_anual')

    #compute -> este campo computado es campo especial donde no lo va meter el usuario, lo vamos a meter nosotros apartir de la fecha de construccion
    
    #COMPUTED FUNCIONALIDAD

    # La funcionalidad que tiene es poder computar es decir vincular a un metodo que nos permita utilizar la iformacion almacenada de ahi, es decir CREA un anclaje para que cuando definamos el decorador junto al metodo nos permita poder vincular la varible de forma correcta.




    #API DEPENDS

    #  ddd



    @api.depends('construido') # ¿De que depende del año del coche? Depende construido -> Cuando el usuario cambie el año construido -> se va disparar automaticamente el metodo.
    def _get_anual(self):
        for coche in self:
            hoy = date.today() # en esta variable se guarda la fecha actual.

            coche.anual = relativedelta(hoy, Coche.construido).years 
            #con el relativedelta se puede calcular la diferencia de año.
            # relativedelta:

               # 1. la variable de la fecha actual
               # 2. la segunda fecha de comparacion)
               # 3. El tipo de fecha que mostrara, si es solamente año, si es dia, si es mes, si es fecha completa. En este caso año.
#------------------------------------------------------------------------------------------------------------

#RESTRICCIONES:

    #restrincciones, mismo formato que en la DB. Esto permite que si selecciona el mismo ID no se puede seleccionar.
    #Fuente: https://www.odoo.com/documentation/15.0/es/developer/howtos/backend.html#model-constraints
    #En otras palabras es una manipulacion de error, si la matricula existe saltara un error en caso contrario el usuario puede continuar con su camino.

    _sql_constrints = [('name_uniq','unique(name)', 'La matricula ya existe, porfavor ingresa otra.' )]
                    #Es una tupla pero espera un arrays.

                    # 1. El campo name sea unico.
                    # 2. El campo que va comprobar que sea unico sera "name"
                    # 3. El mensaje que va mostrar en el caso que exista

#-----------------------------------------------------------------------------------------------------------

class Mantenimiento(models.Model):

    _name ='garaje.Mantenimiento'
    _description ='Permite definir el mantenimiento rutinarios sobre conjuntos de coches.' 
    _order = 'Fecha'
    #name = fields.Char()
    fecha = fields.Date('Fecha', required = True, default = fields.date.today())
    # fields.date.today() -> Me devuelve la fecha de hoy.
    tipo = fields.Selection(string='Tipo', selection=[('l','Lavar'), ('r','Revision'), ('m','Mecanica'), ('p','Pintura')], default='l')
    #Para hacer una seleccion se debe hacer una lista de Tuplas.

    coste = fields.Float('Coste', (8,2), help ='Esto es el coste del mantenimiento total.')

    #Help -> permite darle algo descriptivo al usuario si se llega trabar.

    #-----------------------RELACION ENTRE TABLAS------------------------------------
    Coche_ids = fields.Many2many('garaje.Coche', string='Mantenimiento')

    #CREARA UNA TABLA APARTE PARA QUE PODAMOS CONSULTAR DATOS SERIOS EN LA TABLA.

    #---------------------------------------------------------------------------

    # MANTENIMIENTO CALCULADO

    #Permite que cuando el usuario vea en el calendario la fecha y hora que se va realizar su mantenimiento no lo observe con el garaje.clase,id sino mas bien con un nombre especifico que le daremos. Esto brindara una mejor lectura para el usuario como la administracion.

    def get_name(self):

        for mantenimiento in self:
            #Va crear un campo mediante la variable descripcion que va estar compuesto por id de coches, seguido del costo 

            resultado = [] #lista vacia donde almacenara los resultados.
            descripcion =f'{len(Mantenimiento.Coche_ids)} coches - {Mantenimiento.coste} $'
                    #localizacion clase + variable
            resultado.append()

            
