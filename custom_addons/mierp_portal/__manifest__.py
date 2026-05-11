{
    'name': 'MiERP Portal',
    'version': '1.0.0',
    'summary': 'Portal and website customization for MiERP',
    'description': 'Custom portal for customers and website features',
    'category': 'Website',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'portal',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'installable': True,
    'sequence': 80,
}
