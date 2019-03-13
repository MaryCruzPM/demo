# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models

class contactosherencia(models.Model):
	#los dos de name ya los tiene
	_inherit='res.partner'

	rfcp=fields.Char(
		string="RFC del cliente",
		)