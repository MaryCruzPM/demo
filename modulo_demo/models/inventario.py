from odoo import models, fields, api
from odoo.exceptions import ValidationError

    

class inventario(models.Model):
    _inherit = 'product.template'
   

    @api.onchange('list_price', 'standard_price')
    def _onchange_price(self):
        self.ganancia=self.list_price- self.standard_price
        return{
            'warning':{
                'title':"something bad happened",
                'message':"it was very bad indeed",
            }
        }

   

    ganancia = fields.Integer()
    start_date = fields.Date(default=fields.Date.today)

##valor por default
    
    
    usuarios=fields.Many2many(
        'res.partner',
        string="usuarios que compran producto",  
        domain=[('customer', '=', 'True')],     
        )

    
