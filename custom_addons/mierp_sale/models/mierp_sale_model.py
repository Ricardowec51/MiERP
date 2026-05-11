from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    mierp_sales_channel = fields.Selection(
        [
            ('online', 'Online'),
            ('offline', 'Offline'),
            ('phone', 'Phone'),
            ('partner', 'Partner'),
        ],
        string='Sales Channel',
        default='offline',
    )
    mierp_custom_field = fields.Char(
        string='Custom Field',
        help='Custom field for MiERP Sales',
    )


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    mierp_lead_source = fields.Selection(
        [
            ('website', 'Website'),
            ('email', 'Email'),
            ('phone', 'Phone Call'),
            ('partner', 'Partner'),
            ('event', 'Event'),
        ],
        string='Lead Source',
    )
    mierp_priority_level = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('urgent', 'Urgent'),
        ],
        string='Priority Level',
        default='medium',
    )
