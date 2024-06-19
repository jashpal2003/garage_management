from odoo import fields,models,api

class VehicleDigonis(models.Model):
    _name = 'garage.vehicledigonis'
    _description = 'vehicledigonis'

    name = fields.Many2one('garage.customer','customer name')
    vehicle_problem = fields.Text(related="name.description_of_problem",string='Vehicle problem')
    # vehicle = fields.One2many(related="name.cars", string='vehicle')
    vehicle_brand = fields.Many2one(related="name.company_id", string="vehicle brand name")
    vehicle_model = fields.Many2one(related="name.vehicle_model_id", string='vehicle model name')
    color = fields.Integer("color")
    # department_id = fields.Many2one('garage.department', string='Department')
    # employee_ids = fields.Many2many('garage.employee', string="Employees", compute='_compute_employee_ids', store=False)

    #     Create another model and add a many2many field for this model in the existing
# model but give the table user defined name. Also give user defined name for the
# columns in this table



    # service_needed = fields.Many2many('garage.services','vehicle_service_rel','vehicle_id','service_id',"services",store=True)



    service_needed = fields.Many2many('garage.services','garage_vehicledigonis_id','garage_service_id','garage_vehicledigonis_garage_service_rel',string ='services',store=True)
    # In the many2many field only the records which are ending with ‘ts’ substring
# should be allowed to select.

    # service_needed = fields.Many2many('garage.services',"services",domain="[('name','=like','%ts')]")
    parts_needed_id= fields.One2many('customer.parts',"vehicle_d_id")

    parts_price = fields.Float(compute="_comput_price_depend",string='price for parts')
    service_price = fields.Float(compute="_comput_price_depend",string='price for service')
    total_amount = fields.Float(compute = "_comput_price_depend",string = 'total amount to pay:=')


    additional_box = fields.Boolean('Additional summary')
    summary_text = fields.Text('Summary')

    @api.depends('department_id')
    def _compute_employee_ids(self):
        for record in self:
            if record.department_id:
                record.employee_ids = self.env['garage.employee'].search([('department_id', '=', record.department_id.id)])
            else:
                record.employee_ids = self.env['garage.employee'].browse([])


    @api.depends('parts_needed_id','service_needed')
    def _comput_price_depend(self):
        total_parts_price = 0.0
        total_service_price = 0.0


        for priced in self:
            for pr in priced.parts_needed_id:
                total_parts_price += pr.price
                print(total_parts_price)
            priced.parts_price = total_parts_price
            for sr in priced.service_needed:
                total_service_price += sr.service_price
                print(total_service_price)
            priced.service_price = total_service_price

            priced.total_amount = total_service_price + total_parts_price




                #

                #
                #

    # Add a button on the form view when you click on it, it will link few existing
    # records to the current model’s many2many field


    def link_record(self):

        # ids=[2]
        res1 = self.write({"service_needed": [(6,0,[1 ])]})
        print(" partial remove  ",res1)



class Customer_Parts(models.Model):
    _name = "customer.parts"
    _description = "pasrts for customer"



    vehicle_d_id = fields.Many2one('garage.vehicledigonis','parts_needed_id')
    parts_id = fields.Many2one('garage.parts')
    qty = fields.Integer("qty")

    price = fields.Float("Price")

    @api.depends('qty', 'parts_id')
    def verify_update(self):
        for stock in self:
            stock.parts_id.qty -= stock.qty
            print("______**********__________", stock.parts_id.qty)
        # for x in parts_stock_qty:
        #     print("********************",x.)
        # # for gp in parts_stock_qty:
        # #     print("--------------------------",gp.qty)
        # # # for stock in self:
        # # #     update_qty = parts_stock_qty.qty - stock.qty


    @api.model_create_multi
    def create(self,vals_lst):
        self.verify_update()
        return super().create(vals_lst)






