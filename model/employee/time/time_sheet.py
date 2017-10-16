# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class EmployeeTimesheet(models.Model):
    _name = 'employee.timesheet'

    date = fields.Datetime(string='Date')
    employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee')
    state = fields.Selection([('in', 'IN'), ('out', 'OUT')], string='State')

    def create_attendance(self, rec):
        data = {}
        obj = None
        current_date = datetime.strptime(rec.date, '%Y-%m-%d %H:%M:%S')
        attendance = self.env['employee.attendance.line']

        records = attendance.search([('employee_id', '=', rec.employee_id.id),
                                    ('attendance_id.state', '=', 'draft')])

        for record in records:
            expected_from = datetime.strptime(record.expected_from, '%Y-%m-%d %H:%M:%S') - timedelta(hours=2)
            expected_till = datetime.strptime(record.expected_till, '%Y-%m-%d %H:%M:%S') + timedelta(hours=2)

            if (expected_from <= current_date) and (current_date <= expected_till):
                obj = record

        if rec.state == 'in' and obj:
            if not obj.actual_from:
                data['actual_from'] = rec.date
                obj.write(data)

        if rec.state == 'out' and obj:
            data['actual_till'] = rec.date
            obj.write(data)

    @api.model
    def create(self, vals):
        rec = super(EmployeeTimesheet, self).create(vals)
        self.create_attendance(rec)

        return rec


EmployeeTimesheet()






