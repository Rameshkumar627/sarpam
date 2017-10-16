# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class SalaryRule(models.Model):
    _name = 'salary.rule'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    sequence = fields.Integer(string='Sequence')
    alternate_name = fields.Char(string='Alternate Name')
    percentage = fields.Boolean(string='Percentage')
    percentage_rate = fields.Float(string='Rate (%)')
    slot = fields.Boolean(string='Slot')
    fixed = fields.Boolean(string='Fixed Value')
    formula = fields.Text(string='Formula')

    salary_rule_slot_ids = fields.One2many(comodel_name='salary.rule.slot',
                                           inverse_name='salary_rule_id',
                                           string='Slots')


SalaryRule()


class SalaryRuleSlot(models.Model):
    _name = 'salary.rule.slot'

    from_range = fields.Float(string='From Range')
    till_range = fields.Float(string='Till Range')
    percentage_rate = fields.Float(string='Rate')
    salary_rule_id = fields.Many2one(comodel_name='salary.rule', ondelete='cascade',
                                     string='Salary Rule')


SalaryRuleSlot()
