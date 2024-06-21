from odoo import models,fields,api
class Customer(models.Model):
    _inherit = 'garage.customer'


    customer_work = fields.Char('profession')
    customer_earning = fields.Char('Earning range')


    def print_student(self):
        super().print_student()
        print("extended method called")