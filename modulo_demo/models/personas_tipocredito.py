# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class personas_tipocredito(models.Model):
	"""docstring for ClassName"""
	_name='personas.tipocredito'
	_description='personas tienen ctipo de credito'

	name=fields.Char(
		string="credito",
		)

	tipos=fields.Boolean(
		string="tiene_credito?",
		)