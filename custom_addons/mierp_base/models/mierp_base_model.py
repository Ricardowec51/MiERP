from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    mierp_version = fields.Char(
        'MiERP Version',
        default='1.0.0',
        readonly=True,
    )
    mierp_brand_name = fields.Char(
        'MiERP Brand Name',
        default='MiERP',
    )
    mierp_module_enabled = fields.Boolean(
        'MiERP Enabled',
        default=True,
    )
