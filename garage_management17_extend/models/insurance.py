from odoo import models,fields,api
class Insurance(models.Model):
    _inherit ='garage.services'
    _name= 'garage.insurance'


    accident_description = fields.Char("description of accident")
    accident_time = fields.Date("Date of accident")
    insurance = fields.Float("Insurance Number")
    service_ids= fields.Many2many('garage.services','garage_ainsurance_id', 'garage_service_id', 'garage_insurance_garage_service_rel', string ="service neede")
    parts_id = fields.Many2many('customer.parts','garage_binsurance_id','parts_id','insurance_parts_rel', string = "parts needs to recover the vehicle")