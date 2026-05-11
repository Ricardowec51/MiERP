from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    mierp_employee_code = fields.Char(
        string='Employee Code',
        help='Internal employee code',
    )
    mierp_department_code = fields.Char(
        string='Department Code',
        help='Department code',
    )
    mierp_employment_type = fields.Selection(
        [
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('contract', 'Contract'),
            ('temporary', 'Temporary'),
        ],
        string='Employment Type',
        default='full_time',
    )


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    mierp_custom_notes = fields.Text(
        string='Custom Notes',
        help='Additional notes for payroll',
    )
    mierp_payment_method = fields.Selection(
        [
            ('bank', 'Bank Transfer'),
            ('check', 'Check'),
            ('cash', 'Cash'),
        ],
        string='Payment Method',
    )
