# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class ventas_heredado(models.Model):
	"""docstring for ClassName"""
	_inherit='sale.order'

	tipo_credito=fields.Many2many(
		'personas.tipocredito',
		string="usuarios tienen tipo de credito",
		)

#	ganancia={
#	'ganacia':fields.related('pruduct_id','ganancia',
#		type='Integer', relation='product.template',
#		string="ganancia"),
#	}


#	ganancia=fields.Integer(related='product_id.ganancia')

