# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api


class add_fields(models.Model):
	"""docstring for ClassName"""
	_inherit='product.template'


	x_autor=fields.Many2one('res.partner',#modelo de donde saca los atributos
										string="autor",
										)
	
	x_editorial=fields.Many2one('res.partner',
										string="editorial",
										)

