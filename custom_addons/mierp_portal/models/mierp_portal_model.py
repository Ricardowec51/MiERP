from odoo import models, fields


class PortalCustomization(models.Model):
    _name = 'mierp.portal.config'
    _description = 'Portal Configuration'

    name = fields.Char(
        string='Portal Name',
        default='MiERP Portal',
    )
    custom_theme = fields.Selection(
        [
            ('light', 'Light'),
            ('dark', 'Dark'),
            ('blue', 'Blue'),
            ('green', 'Green'),
        ],
        string='Theme',
        default='light',
    )
    enable_analytics = fields.Boolean(
        string='Enable Analytics',
        default=True,
    )
    portal_description = fields.Text(
        string='Portal Description',
        help='Portal description for public access',
    )
