# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class EmployeeAttendance(models.Model):
    _name = 'employee.attendance'

    date = fields.Date(string='Date')
    comment = fields.Text(string='Comment')
    state = fields.Selection([('draft', 'Draft'),
                              ('check', 'Check'),
                              ('confirmed', 'Confirmed')], string='State')
    checked_on = fields.Date(string='Checked On')
    checked_by = fields.Many2one(comodel_name='hospital.employee', string='Checked By')
    attendance_line_ids = fields.One2many(comodel_name='employee.attendance.line',
                                          inverse_name='attendance_id',
                                          string='Attendance Line')

    @api.multi
    def check_button(self):
        data = {}
        data['state'] = 'check'
        attendances = self.attendance_line_ids
        time_config = self.env['time.configuration'].search([('name', '=', 'Time Delay')])
        half_day = time_config.half_day
        full_day = time_config.full_day

        for attendance in attendances:
            attendance_state = None
            if (attendance.actual_time >= half_day) and (attendance.actual_time <= full_day):
                attendance_state = 'half_day'
            elif attendance.actual_time >= full_day:
                attendance_state = 'full_day'
            elif attendance.is_week_off:
                attendance_state = 'week_off'
            else:
                attendance_state = 'absent'

            attendance.write({'day_state': attendance_state})

        self.write(data)

    @api.multi
    def confirmed_button(self):
        data = {}
        data['state'] = 'confirmed'
        self.write(data)


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
                                  ('week_off', 'Week-Off'),
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
