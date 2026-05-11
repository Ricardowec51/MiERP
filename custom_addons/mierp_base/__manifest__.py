{
    'name': 'MiERP Base',
    'version': '1.0.0',
    'summary': 'Base configuration and branding for MiERP',
    'description': 'Base module providing core functionality and branding for MiERP custom modules',
    'category': 'Tools',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_base_views.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': 1,
}
