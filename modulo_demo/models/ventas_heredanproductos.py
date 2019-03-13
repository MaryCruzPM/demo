# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class ventas_heredadop(models.Model):
	"""docstring for ClassName"""
	_inherit='sale.order.line'


	ganancia=fields.Integer(related='product_id.ganancia')