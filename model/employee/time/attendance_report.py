# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class AttendanceReport(models.AbstractModel):
    _name = 'report.sarpam.attendance_report'

    @api.multi
    def render_html(self, docids, data=None):
        return data['html']


AttendanceReport()


class AttendanceWizard(models.TransientModel):
    _name = 'attendance.wizard'

    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')

    def get_dates_in_month(self, start_date, end_date):
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        dates = (end_date_obj - start_date_obj).days

        list_days = []
        for day in range(0, dates):
            list_days.append((start_date_obj + timedelta(days=day)).strftime("%Y-%m-%d"))

        return list_days

    @api.multi
    def print_report(self):
        start_day = self.start_date
        end_day = self.end_date
        days = self.get_dates_in_month(start_day, end_day)

        dict_attendance_record = self.calculate_employee_attendance(days)
        dict_attendance_summary = self.calculate_employee_summary(dict_attendance_record, start_day, end_day)

        obj = self.env['hospital.patient'].search([('id', '>', 0)])
        html = self.update_html(dict_attendance_summary, dict_attendance_record, days)
        datas = {'html': html}

        data = self.env['report'].get_action(obj, 'sarpam.organisational_chart', data=datas)

        return data

    def calculate_employee_attendance(self, days):
        dict_rec = {}
        employees = self.env['hospital.employee'].search([('id', '>', 0)])

        for day in days:
            for employee in employees:
                rec = self.env['employee.attendance.line'].search([('attendance_id.date', '>=', day),
                                                                   ('attendance_id.date', '<=', day),
                                                                   ('employee_id', '=', employee.id),
                                                                   ('attendance_id.state', '=', 'confirmed')])

                if rec:
                    dict_rec[day] = {employee.employee_uid: {'state': rec.day_state,
                                                             'Week-Off': rec.is_week_off}}

        return dict_rec

    def calculate_employee_summary(self, dict_rec, start_day, end_day):
        dict_emp = {}
        days = self.get_dates_in_month(start_day, end_day)
        employees = self.env['hospital.employee'].search([('id', '>', 0)])

        for employee in employees:
            total_days = 0
            present_days = 0
            absent_days = 0
            week_off_days = 0

            for day in days:
                if day in dict_rec:
                    total_days = total_days + 1
                    if dict_rec[day][employee.employee_uid]['state'] == 'full_day':
                        present_days = present_days + 1
                    elif dict_rec[day][employee.employee_uid]['state'] == 'half_day':
                        present_days = present_days + .5
                        absent_days = absent_days + .5
                    elif dict_rec[day][employee.employee_uid]['state'] == 'absent':
                        absent_days = absent_days + 1

                    if dict_rec[day][employee.employee_uid]['Week-Off']:
                        week_off_days = week_off_days + 1

            dict_emp[employee.employee_uid] = {'Total Days': total_days,
                                               'Present Days': present_days,
                                               'Absent Days': absent_days,
                                               'Week-Off Days': week_off_days}

        return dict_emp

    def update_html(self, dict_emp, dict_attendance, dates):
        start_header = '<tr><th>S.No</th><th>Name</th><th>Employee ID</th>'
        end_header = '<th>Total Days</th><th>Present days</th><th>Absent days</th><th>Week-Off days</th></tr>'
        mid_header = ''
        attendance = ''

        employees = self.env['hospital.employee'].search([('id', '>', 0)])

        for date in dates:
            mid_header = '{0}<th>{1}</th>'.format(mid_header, date)

        title = '{0}{1}{2}'.format(start_header, mid_header, end_header)
        count = 0
        for employee in employees:
            count = count + 1
            attendance = '{0}<tr>'.format(attendance)
            attendance = '{0}<td>{1}</td>'.format(attendance, count)
            attendance = '{0}<td>{1}</td>'.format(attendance, employee.name)
            attendance = '{0}<td>{1}</td>'.format(attendance, employee.employee_uid)
            for date in dates:
                if date in dict_attendance:
                    state = dict_attendance[date][employee.employee_uid]['state']
                    attendance = '{0}<td class="{1}"></td>'.format(attendance, state)
                else:
                    attendance = '{0}<td></td>'.format(attendance)

            employee_dict = dict_emp[employee.employee_uid]
            attendance = '{0}<td class="vals">{1}</td>'.format(attendance, employee_dict['Total Days'])
            attendance = '{0}<td class="vals">{1}</td>'.format(attendance, employee_dict['Present Days'])
            attendance = '{0}<td class="vals">{1}</td>'.format(attendance, employee_dict['Absent Days'])
            attendance = '{0}<td class="vals">{1}</td>'.format(attendance, employee_dict['Week-Off Days'])
            attendance = '{0}</tr>'.format(attendance)

        table = '<table style="width:100%">{0}{1}</table>'.format(title, attendance)
        html = '''<!DOCTYPE html>
                    <html>
                    <head>
                    <style>
                    table {{
                        font-family: arial, sans-serif;
                        border-collapse: collapse;
                        width: 100%;
                        border: 1px solid black;
                    }}

                    td, th {{
                        border: 1px solid black;
                        text-align: left;
                        padding: 8px;
                        width: 150px;
                        height: 80px;
                    }}

                    .half_day {{ background-color: blue; }}
                    .absent {{ background-color: red; }}
                    .week_off {{ background-color: yellow; }}
                    .vals {{ text-align: center;}}

                    tr:nth-child(even) {{
                        background-color: #dddddd;
                    }}
                    </style>
                    </head>
                    <body>
                    {0}
                    </body>
                    </html>
                    '''.format(table)

        return html


AttendanceWizard()


