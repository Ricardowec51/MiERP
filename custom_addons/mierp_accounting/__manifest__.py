{
    'name': 'MiERP Accounting',
    'version': '1.0.0',
    'summary': 'Accounting and financial management for MiERP',
    'description': 'Manage invoices, payments, journals, and financial reports',
    'category': 'Accounting',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_accounting_views.xml',
    ],
    'installable': True,
    'sequence': 40,
}
