# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta
from calendar import monthrange


class PaySlip(models.Model):
    _name = 'pay.slip'

    name = fields.Many2one(comodel_name='hospital.employee', string='Name')
    from_date = fields.Date(string='From Date')
    till_date = fields.Date(string='Till Date')
    salary_setting = fields.Many2one(comodel_name='salary.wages')
    salary_structure = fields.Many2one(comodel_name='salary.structure',
                                       related='salary_setting.salary_structure',
                                       string='Salary Structure')

    pay_slip_lines = fields.One2many(comodel_name='pay.slip.line',
                                     inverse_name='pay_slip_id',
                                     string='Pay Slip Lines')

    pay_slip_data_lines = fields.One2many(comodel_name='pay.slip.data.line',
                                          inverse_name='pay_slip_id',
                                          string='Pay Slip Data Lines')

    local_dict = {}

    def check_date(self):
        if self.from_date > self.till_date:
            raise exceptions.ValidationError('Error! Till date greater than From Date ')

        from_date = datetime.strptime(self.from_date, '%Y-%m-%d')
        till_date = datetime.strptime(self.till_date, '%Y-%m-%d')

        if (from_date.month != till_date.month) and (from_date.year != till_date.year):
            raise exceptions.ValidationError('Error! From and Till date must be within a month')

    def compute_day_wage(self, obj):
        '''Day Wages = Actual wage - lop'''

        salary = total_days = month_days = lop_days = 0
        data = {}

        from_date = datetime.strptime(self.from_date, '%Y-%m-%d')
        till_date = datetime.strptime(self.till_date, '%Y-%m-%d')

        total_days = (till_date - from_date).days

        month_days = monthrange(from_date.year, from_date.month)[1]

        if not (self.salary_setting and self.salary_structure):
            raise exceptions.ValidationError('Error! Salary Structure and wages required for further progress')

        if obj.type == 'monthly':
            salary = obj.wage / month_days
        elif obj.type == 'weekly':
            salary = obj.wage / 7
        elif obj.type == 'daily':
            salary = obj.wage

        data['total_days'] = total_days
        data['lop_days'] = 0

        self.write(data)
        value = (salary * total_days) - (salary * lop_days)
        return value

    @api.multi
    def amount_calculation(self, rule):
        data = {}

        data['name'] = rule.name
        data['code'] = rule.code
        data['alternate_name'] = rule.alternate_name

        data['rule'] = rule.id
        data['pay_slip_id'] = self.id

        if rule.fixed:
            data['rate'] = 0
            data['amount'] = eval(rule.formula, self.local_dict)

        elif rule.percentage:
            data['rate'] = float(rule.percentage_rate/100)
            data['amount'] = eval(rule.formula, self.local_dict) * data['rate']

        elif rule.slot:
            val = eval(rule.formula, self.local_dict)

            for slot in rule.salary_rule_slot_ids:
                if slot.from_range < val < slot.till_range:
                    data['amount'] = val * (float(slot.percentage_rate)/100)
                    data['rate'] = slot.percentage_rate

        self.pay_slip_lines.create(data)
        self.local_dict[rule.code] = data['amount']

    @api.multi
    def on_execution(self):
        self.check_date()
        self.pay_slip_lines.unlink()
        rules = self.salary_structure.salary_rule_ids

        rule_lists = []
        for rule in rules:
            rule_lists.insert(rule.sequence, rule)

        wage_obj = self.env['salary.wages'].search([('name', '=', self.name.id)])
        self.local_dict['WAGE'] = self.compute_day_wage(wage_obj)
        for rule in rule_lists:
            local_dict = self.amount_calculation(rule.name)

PaySlip()


class PaySlipLine(models.Model):
    _name = 'pay.slip.line'

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    alternate_name = fields.Char(string='Alternate Name')
    rule = fields.Many2one(comodel_name='salary.rule', string='Rule')
    amount = fields.Float(string='Amount')

    pay_slip_id = fields.Many2one(comodel_name='pay.slip', string='Pay Slip')


PaySlipLine()


class PaySlipDataLine(models.Model):
    _name = 'pay.slip.data.line'

    name = fields.Many2one(comodel_name='payslip.info', string='Data', required=True)
    value = fields.Float(string='Value')

    pay_slip_id = fields.Many2one(comodel_name='pay.slip', string='Pay Slip')


PaySlipDataLine()


class PayslipInfo(models.Model):
    _name = 'payslip.info'

    name = fields.Char(string='Name')


PayslipInfo()