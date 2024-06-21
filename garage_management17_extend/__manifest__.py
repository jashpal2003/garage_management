{
    'name':'garage management extended',
    'description':'this module is used to manage the garage',
    'author':'jashpal',
    'website':'https://pythonicprince.odoo.com/',
    'version':'1.0',
    'depends':['base','web','garage_management17'],
    'data':[
        'security/garage_security.xml',
        'security/ir.model.access.csv',
        'views/customer_view.xml',
        'views/insurance_view.xml',
    ],
    'auto_install':True,
    'installable':True,
    'application':True,

}