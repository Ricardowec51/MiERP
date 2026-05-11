{
    'name': 'MiERP Human Resources',
    'version': '1.0.0',
    'summary': 'HR and payroll management for MiERP',
    'description': 'Manage employees, contracts, leaves, and payroll',
    'category': 'Human Resources',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'hr',
        'hr_payroll',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_hr_views.xml',
    ],
    'installable': True,
    'sequence': 50,
}
