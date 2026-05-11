{
    'name': 'MiERP Sales',
    'version': '1.0.0',
    'summary': 'Sales and CRM management for MiERP',
    'description': 'Manage sales orders, opportunities, and customer relationships',
    'category': 'Sales',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'sale',
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_sale_views.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': 10,
}
