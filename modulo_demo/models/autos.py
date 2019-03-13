# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class Autos(models.Model):

	_name='personas.autos'
	_description='personas que estan relacionas con auto'

	name=fields.Char(
		string="matricula",
		)

	color=fields.Char(
		string="color",
		)

	anio=fields.Char(
		string="año",
		)

	persona_id=fields.Many2one(
		'persona.main_data',
		string="persona",
		)