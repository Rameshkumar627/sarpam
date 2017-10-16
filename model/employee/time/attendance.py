# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class EmployeeAttendance(models.Model):
    _name = 'employee.attendance'

    date = fields.Date(string='Date')
    comment = fields.Text(string='Comment')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], string='State')
    attendance_line_ids = fields.One2many(comodel_name='employee.attendance.line',
                                          inverse_name='attendance_id',
                                          string='Attendance Line')

    @api.multi
    def calculate_day_status(self):
        pass


EmployeeAttendance()


class EmployeeAttendanceLine(models.Model):
    _name = 'employee.attendance.line'

    employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee')
    expected_from = fields.Datetime(string='Expected From')
    expected_till = fields.Datetime(string='Expected Till')
    expected_time = fields.Float(string='Expected Time', compute='get_expected_time', store=False)
    actual_from = fields.Datetime(string='Actual From')
    actual_till = fields.Datetime(string='Actual Till')
    actual_time = fields.Float(string='Actual Time', store=False)
    day_state = fields.Selection([('full_day', 'Full Day'),
                                  ('half_day', 'Half Day'),
                                  ('absent', 'Absent')],
                                 string='Day status')
    is_week_off = fields.Boolean(string='Week Off')
    attendance_id = fields.Many2one(comodel_name='employee.attendance', string='Attendance')
    shift = fields.Many2one(comodel_name='employee.shift', string='Shift')
    comment = fields.Text(string='Comment')

    def get_expected_time(self):
        if self.expected_till and self.expected_from:
            expected_till = datetime.strptime(self.expected_till, "%Y-%m-%d %H:%M:%S")
            expected_from = datetime.strptime(self.expected_from, "%Y-%m-%d %H:%M:%S")
            self.expected_time = float((expected_till - expected_from).seconds) / 3600

        if self.actual_till and self.actual_from:
            print "ramesh"
            actual_till = datetime.strptime(self.actual_till, "%Y-%m-%d %H:%M:%S")
            actual_from = datetime.strptime(self.actual_from, "%Y-%m-%d %H:%M:%S")
            self.actual_time = float((actual_till - actual_from).seconds) / 3600

    _sql_constraints = [('uniq_name', 'unique(employee_id, attendance_id)', _("Employee must be unique !"))]


EmployeeAttendanceLine()
