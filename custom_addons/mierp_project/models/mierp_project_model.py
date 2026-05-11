from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    mierp_project_code = fields.Char(
        string='Project Code',
        help='Internal project code',
    )
    mierp_priority = fields.Selection(
        [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('critical', 'Critical'),
        ],
        string='Priority',
        default='medium',
    )


class ProjectTask(models.Model):
    _inherit = 'project.task'

    mierp_task_type = fields.Selection(
        [
            ('development', 'Development'),
            ('testing', 'Testing'),
            ('documentation', 'Documentation'),
            ('support', 'Support'),
            ('other', 'Other'),
        ],
        string='Task Type',
    )
    mierp_estimated_hours = fields.Float(
        string='Estimated Hours',
    )
