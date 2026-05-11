from odoo import models, fields


class MierpHelpdeskTicket(models.Model):
    _name = 'mierp.helpdesk.ticket'
    _description = 'Helpdesk Ticket'
    _inherit = ['mail.thread']

    name = fields.Char(
        string='Ticket Number',
        default='/',
        readonly=True,
    )
    subject = fields.Char(
        string='Subject',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
    )
    assigned_to = fields.Many2one(
        'res.users',
        string='Assigned To',
    )
    status = fields.Selection(
        [
            ('new', 'New'),
            ('open', 'Open'),
            ('in_progress', 'In Progress'),
            ('pending', 'Pending'),
            ('closed', 'Closed'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='new',
    )
    priority = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('urgent', 'Urgent'),
        ],
        string='Priority',
        default='medium',
    )
    created_date = fields.Datetime(
        string='Created Date',
        default=fields.Datetime.now,
    )
    updated_date = fields.Datetime(
        string='Updated Date',
        default=fields.Datetime.now,
    )
