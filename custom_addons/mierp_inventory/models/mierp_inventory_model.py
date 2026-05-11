from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    mierp_sku_custom = fields.Char(
        string='Custom SKU',
        help='Custom SKU for internal inventory tracking',
    )
    mierp_storage_location = fields.Char(
        string='Storage Location',
        help='Location in warehouse',
    )
    mierp_reorder_level = fields.Integer(
        string='Reorder Level',
        default=0,
    )


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    mierp_movement_type = fields.Selection(
        [
            ('in', 'Inbound'),
            ('out', 'Outbound'),
            ('internal', 'Internal Transfer'),
        ],
        string='Movement Type',
    )
    mierp_notes = fields.Text(
        string='Movement Notes',
    )
