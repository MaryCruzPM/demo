# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class NombreCuentasEmail(models.Model):

	_name='personas.grado_estudio' #nombre del modelo
	_description='personas tienen grado de estudio'
	
	name =fields.Char(
		string="Nivel de estudios",
		required=True,
		)
	
	anios=fields.Integer(
		string="años de estudio",
		)