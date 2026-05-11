from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    mierp_document_type = fields.Selection(
        [
            ('invoice', 'Invoice'),
            ('credit', 'Credit Note'),
            ('debit', 'Debit Note'),
        ],
        string='Document Type',
    )
    mierp_custom_reference = fields.Char(
        string='Custom Reference',
        help='Custom reference for internal tracking',
    )
    mierp_department = fields.Char(
        string='Department',
        help='Department responsible for the move',
    )


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    mierp_journal_category = fields.Selection(
        [
            ('sales', 'Sales'),
            ('purchases', 'Purchases'),
            ('bank', 'Bank'),
            ('cash', 'Cash'),
            ('miscellaneous', 'Miscellaneous'),
        ],
        string='Journal Category',
    )
