# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class SalaryWages(models.Model):
    _name = 'salary.wages'

    name = fields.Many2one(comodel_name='hospital.employee')
    salary_structure = fields.Many2one(comodel_name='salary.structure', string='Salary Structure')
    wage = fields.Float(string='Wage')
    type = fields.Selection([('daily', 'Daily'),
                             ('weekly', 'Weekly'),
                             ('monthly', 'Monthly')],
                            string='Type')


SalaryWages()
