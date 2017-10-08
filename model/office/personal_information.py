# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Education(models.Model):
    _name = 'employee.education'

    name = fields.Many2one(comodel_name='human.course', string='Course')
    hospital_employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee')
    duration = fields.Integer(string='Course (In Years)')
    percentage = fields.Integer(string='Percentage/CGPA')
    academy = fields.Char(string='University/ School')
    status = fields.Selection([('pass', 'Pass'),
                               ('fail', 'Fail')],
                              string='Pass/ Fail')
    comment = fields.Text(string='Comment')


Education()


class Course(models.Model):
    _name = 'human.course'

    name = fields.Char(string='Name of the course')


Course()


class Awards(models.Model):
    _name = 'employee.awards'

    name = fields.Char(string='Name of the award')
    hospital_employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee')
    attachment = fields.Binary(string='Attachments')
    comment = fields.Text(string='Comment')


Awards()


class Experience(models.Model):
    _name = 'employee.experience'

    name = fields.Char(string='Comapny Name')
    duration = fields.Integer(string='Duration (In Years)')
    position = fields.Integer(string='Position')
    leaving_reason = fields.Char(string='Reason for leaving')
    comment = fields.Text(string='Comment')
    hospital_employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee')


Experience()


class EmployeeType(models.Model):
    _name = 'employee.type'

    name = fields.Char(string='Employee Type')


EmployeeType()
