from odoo import models, fields, api
from odoo.exceptions import ValidationError

    
class dependsModel(models.Model):
    _name = 'test.computed'


    @api.depends('value')
    def _compute_depends(self):
        for record in self:
            record.name = "Record with value %s" % record.value

    @api.onchange('amount', 'precio_unit')
    def _onchange_price(self):
        self.precio=self.amount * self.precio_unit
        return{
            'warning':{
                'title':"something bad happened",
                'message':"it was very bad indeed",
            }
        }

    @api.constrains('age')
    def _check_something(self):
        for record in self:
            if record.age > 20:
                raise ValidationError("your record is too old: %s" % record.age)


    name = fields.Char(compute='_compute_depends')
    value = fields.Integer()

##valor por default
    
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    precio=fields.Integer()
    precio_unit=fields.Integer()
    amount=fields.Integer()
    age=fields.Integer()