{
    'name':'Garage Management',
    'description':'this is garage management module',
    'author':'jashpal',
    'website':'https://www.jashpal.com',
    'version':'1.0',
    'depends':['base','mail','web'],
    'data':['security/garage_security.xml',
            'security/ir.model.access.csv',
            'data/customer_sequence.xml',
            'views/customer_view.xml',
            'views/vehicle_view.xml',
            'views/employees_view.xml',
            'views/services_view.xml',
            'views/parts_view.xml',
            'views/billing_view.xml',
            'views/vehicledigonis_view.xml',
            'views/department_view.xml',
            ],

    'assets':{
        'web.assets_backend':[
            'garage_management/static/src/scss/jashpal_style.scss'
        ],
    },
    'auto_install':False,
    'installable':True,
    'application':True,
}