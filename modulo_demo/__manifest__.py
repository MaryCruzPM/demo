# -*- coding: utf-8 -*-
{
'name': "Modulo de muestra",
'sumary': """
mi modulo de muestra
""",
'description': """
Probando modulo con clases
""",
'author': "Soluciones 4G",
'website': "http:www.soluciones4g.com",

'category': 'pruebas',
'version': '1.0',

'depends': [
'base',
'contacts',
'stock',
'sale_management',
'sale',
],

'data':[
'views/persona_view.xml',
'views/contactoheredado.xml',
'views/productoheredado.xml',
'views/ventasheredado.xml',
'views/computer.xml',
'views/dependencia.xml',
'data/personas_demo.xml',
'security/ir.model.access.csv',

],

'installable':True,
'auto_install':False,

}