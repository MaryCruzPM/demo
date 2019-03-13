# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class nombrecuentasemail(models.Model):
	"""docstring for ClassName"""
	_name='personas.nombre_cuentas_email'
	_description='personas tienen cuentas email'

	name=fields.Char(
		string="Dominio",
		required=True,
		)

	dominio_publico=fields.Boolean(
		string="el dominio publico?",
		)