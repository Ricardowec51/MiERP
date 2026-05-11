{
    'name': 'MiERP Projects',
    'version': '1.0.0',
    'summary': 'Project and task management for MiERP',
    'description': 'Manage projects, tasks, and time tracking',
    'category': 'Projects',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_project_views.xml',
    ],
    'installable': True,
    'sequence': 60,
}
