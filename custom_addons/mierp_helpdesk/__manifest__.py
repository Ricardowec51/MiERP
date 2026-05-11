{
    'name': 'MiERP Helpdesk',
    'version': '1.0.0',
    'summary': 'Support and ticket management for MiERP',
    'description': 'Manage support tickets and customer issues',
    'category': 'Services',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_helpdesk_views.xml',
    ],
    'installable': True,
    'sequence': 70,
}
