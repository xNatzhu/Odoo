# -*- coding: utf-8 -*-
{
    'name': "SportService",

    'summary': """""",

    'description': """
        Aplicacion orientada al area de servicios
    """,

    'author': "Agustin Saravia",
    'website': "http://https://www.vangrow.ar/",


    'category': 'Uncategorized',
    'version': '1.1',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'mail',],

    # always loaded
    'data': [
        'security/sportservice_security.xml',
        'security/ir.model.access.csv',
        'views/sportservice_views.xml',
        'views/sportservice_cliente_views.xml',
        'views/templates.xml',
       
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}