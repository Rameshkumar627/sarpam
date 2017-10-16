# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class SalaryStructure(models.Model):
    _name = 'salary.structure'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    salary_rule_ids = fields.One2many(comodel_name='salary.structure.rule',
                                      inverse_name='salary_structure_id',
                                      string='Salary Rule')


SalaryStructure()


class SalaryStructureRule(models.Model):
    _name = 'salary.structure.rule'

    name = fields.Many2one(comodel_name='salary.rule', string='Salary Structure Rule')
    code = fields.Char(string='Code', related='name.code')
    sequence = fields.Integer(string='Sequence', related='name.sequence')
    alternate_name = fields.Char(string='Alternate Name', related='name.alternate_name')

    salary_structure_id = fields.Many2one(comodel_name='salary.structure', string='Salary Structure')


SalaryStructureRule()




