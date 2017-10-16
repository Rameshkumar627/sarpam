# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class SalaryBatch(models.Model):
    _name = 'salary.batch'

    name = fields.Char(string='Batches')
    from_date = fields.Date(string='From Date')
    till_date = fields.Date(string='Till Date')
    employee_ids = fields.One2many(comodel_name='salary.batch.employee',
                                   inverse_name='salary_batch_id',
                                   string='Employees')

    @api.multi
    def pay_slip_create(self):
        recs = self.employee_ids
        pay_slip = self.env['pay.slip']
        wage_obj = self.env['salary.wages']

        for rec in recs:
            data = {}
            wage = wage_obj.search([('name', '=', rec.id)])
            data['from_date'] = self.from_date
            data['till_date'] = self.till_date
            data['name'] = rec.id
            data['salary_setting'] = wage.id

            pay_slip.create(data)


SalaryBatch()


class SalaryBatchEmployee(models.Model):
    _name = 'salary.batch.employee'

    name = fields.Many2one(comodel_name='hospital.employee', string='Employee')
    salary_batch_id = fields.Many2one(comodel_name='salary.batch', string='Batch')


SalaryBatchEmployee()
