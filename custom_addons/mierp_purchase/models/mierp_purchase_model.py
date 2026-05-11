from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    mierp_purchase_type = fields.Selection(
        [
            ('standard', 'Standard'),
            ('emergency', 'Emergency'),
            ('blanket', 'Blanket Order'),
        ],
        string='Purchase Type',
        default='standard',
    )
    mierp_supplier_rating = fields.Integer(
        string='Supplier Rating',
        help='Rating from 1 to 5',
        default=0,
    )


class ResPartner(models.Model):
    _inherit = 'res.partner'

    mierp_is_supplier = fields.Boolean(
        string='Is Supplier',
        help='Check if this partner is a supplier',
    )
    mierp_supplier_code = fields.Char(
        string='Supplier Code',
        help='Internal code for supplier',
    )
