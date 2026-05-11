{
    'name': 'MiERP Inventory',
    'version': '1.0.0',
    'summary': 'Inventory and warehouse management for MiERP',
    'description': 'Manage products, stock movements, and warehouse operations',
    'category': 'Inventory',
    'author': 'MiERP Development Team',
    'website': 'https://github.com/Ricardowec51/MiERP',
    'license': 'MIT',
    'depends': [
        'mierp_base',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/mierp_inventory_views.xml',
    ],
    'installable': True,
    'sequence': 30,
}
