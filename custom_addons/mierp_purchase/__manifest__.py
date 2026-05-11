{
    'name': 'MiERP Purchases',
    'version': '1.0.0',
    'summary': 'Purchase orders and supplier management for MiERP',
    'description': 'Manage purchase orders, vendors, and procurement processes',
    'category': 'Purchases',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_purchase_views.xml',
    ],
    'installable': True,
    'sequence': 20,
}
