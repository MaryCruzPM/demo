# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models



class persona(models.Model): #
	_name = 'persona.main_data'
	_description='persona'
	
	name =fields.Char(
		string="nombre de la persona",
		required=True,
		help="esta es la ayuda para el nombre",
		index=True,
		)
	edad = fields.Integer( 
		string="edad de la persona",
		default =15,
		required=True,
		)

	es_casado=fields.Boolean( string="es casado?",
		)

	datos_personales=fields.Html(
		string="datos_personales",
		)
	informacion_adicional=fields.Text(
		string="informacio_adicional",
		)
	foto=fields.Binary(
		string="foto",
		help="agrega una foto",
		)
	sexo=fields.Selection(
		selection=[('femenino','Femenino'),('masculino','Masculino'),
		('otro','otro')],
		string="Sexo",
		required=True,
		default="otro",
		)

	grado_estudio_id=fields.Many2one('personas.grado_estudio',
										string="grado_maximo_estudio",
										)

	dominio_email_ids=fields.Many2many(
		'personas.nombre_cuentas_email',
		string="dominios de correo",		
		)

	autos_ids=fields.One2many(
		'personas.autos',
		'persona_id',
		string="autos",
		)

	_sql_constraints=[
	('verificacion de nombre',
	 'CHECK(edad>18)',
	 "Tiene que tener mas de 18, el campo no puede estar vacio"),
	]
