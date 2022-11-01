# -*- coding: utf-8 -*-
{
    'name': "garaje", # El nombre del modulo.

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""", #---------Descripcion del modulo. Aqui se pone una descripcion corta---------


    'description': """
        Long description of module's purpose
    """, #--------Esta es una descripcion como antes pero mas desarrollada mas larga.--------


    'author': "Agustin Saravia", # El nombre del autor del modulo.

    'website': "http://www.yourcompany.com",  # Aca es cuando tenemos una web de consulta lo dirigimos con este enlace.


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list


    'category': 'Uncategorized', # Las categorias disponibles para los modulos de la tienda.
    'version': '0.2', # La version se puede incrementar a medidas que se vayan subiendo las actualizaciones. El primer numero es para los mayores, y el segundo para los intermedio.

    # any module necessary for this one to work correctly

    'depends': ['base'], # La dependecia sirve para añadir los modulos que requerimos para poder intengtarlo. Esto lo hacemos por , -> 'depends': ['base', "Sales", "ect"].

    #Esto permite que cuando instale mi modulo va exigir el sistema que tambien instale los otros modulos. 



    # always loaded
    'data': [
        #Se carga siempre todos los datos precargados que hemos configurado en la data. Al contrario al demo en este caso se descargan automaticamente.
        'security/garaje_segurity.xml', #El archivo xml debe ir primero, ya que debe leer primero la secuencia del xml y luego el csv
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml', # datos permanente. Es decir que no hay necesidad de pedir permiso para cargarlo, lo carga automaticamente,
        'data/garaje_data.xml', #es el template solo que lo haremos en la data.
    ],
    # only loaded in demonstration mode
    'demo': [
        #El demo esta configurada con datos de pruebas. Eso no lo cargara al menos que nosotros le solicitemos recargar los datos de demostracion.
        'demo/demo.xml', # modo de demostracion - datos temporales
    ],

    #EN ODOO SE TRABAJA CON DOS TIPOS DE FICHEROS PY (PYTHON) Y XML (VISTAS, INFORMES, DATOS, ECT)

    #PARA INDICAR QUE ES UNA APLICACION EL MODULO SE HACE DE ESTA MANERA.

    'application':True, # Ahora va detectar Odoo como una aplicacion en el sistema en el modulo.
}