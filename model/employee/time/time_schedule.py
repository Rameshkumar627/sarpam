# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta
import math


def date_range(from_date, till_date):
    days = datetime.strptime(till_date, '%Y-%m-%d') - datetime.strptime(from_date, '%Y-%m-%d')
    return days.days + 1


class EmployeeTimeSchedule(models.Model):
    _name = 'employee.time.schedule'

    sequence = fields.Char(string='Sequence', readonly=True)
    from_date = fields.Date(string='From Date', required=True)
    till_date = fields.Date(string='Till Date', required=True)
    shift = fields.Many2one(comodel_name='employee.shift', string='Shift', required=True)
    comment = fields.Text(string='Comment')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], string='State')
    schedule_line_ids = fields.One2many(comodel_name='employee.time.schedule.line',
                                        inverse_name='schedule_id',
                                        string='Employee')

    def create_attendance(self):
        attendance = self.env['employee.attendance']
        attendance_line = self.env['employee.attendance.line']
        start_hours = self.shift.from_time_hours
        start_mins = self.shift.from_time_min
        duration = self.shift.duration

        days = date_range(self.from_date, self.till_date)
        start_date = datetime.strptime(self.from_date, '%Y-%m-%d')

        attendance_data = {}
        for day in range(0, days):
            date = start_date + timedelta(days=day)
            attendance_data['date'] = date.strftime('%Y-%m-%d')
            attendance_data['state'] = 'draft'
            attendance_obj = attendance.create(attendance_data)
            recs = self.schedule_line_ids

            attendance_line_data = {}
            for rec in recs:
                expected_from = (date + timedelta(hours=start_hours, minutes=start_mins)) - timedelta(hours=5, minutes=30)
                expected_till = (expected_from + timedelta(hours=duration)).strftime("%Y-%m-%d %H:%M:%S")
                attendance_line_data['employee_id'] = rec.employee_id.id
                attendance_line_data['expected_from'] = expected_from.strftime("%Y-%m-%d %H:%M:%S")
                attendance_line_data['expected_till'] = expected_till
                attendance_line_data['shift'] = self.shift.id
                attendance_line_data['attendance_id'] = attendance_obj.id
                attendance_line.create(attendance_line_data)

    @api.multi
    def confirm_button(self):
        self.create_attendance()
        self.write({'state': 'confirmed'})


EmployeeTimeSchedule()


class EmployeeTimeScheduleLine(models.Model):
    _name = 'employee.time.schedule.line'

    employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee', required=True)
    schedule_id = fields.Many2one(comodel_name='employee.time.schedule', string='Schedule')


EmployeeTimeScheduleLine()


