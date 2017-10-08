# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Employee(models.Model):

    _name = 'hospital.employee'

    # Official Information
    image = fields.Binary(string='Image')
    position = fields.Char(string='Job Position')
    name = fields.Char(string='Employee Name', required=True)
    employee_uid = fields.Char(string='Employee ID')
    employee_type = fields.Many2one(comodel_name='employee.type', string='Employee Type', required=True)
    date_of_join = fields.Date(string='Date Of Joining')
    date_of_exit = fields.Date(string='Date Of Exit')
    phone_primary = fields.Char(string='Phone Primary')
    phone_secondary = fields.Char(string='Phone Secondary')
    email = fields.Char(string='Email', required=True)
    pan = fields.Char(string='PAN', required=True)
    aadhar_card = fields.Char(string='Aadhar Card')
    bank_name = fields.Many2one(comodel_name='account.bank', string='Bank')
    account_no = fields.Char(string='Bank Account No')
    direct_reportee = fields.Many2one(comodel_name='hospital.employee', string='Direct Reportee', index=True)
    subordinates = fields.One2many(comodel_name='hospital.employee',
                                   inverse_name='direct_reportee',
                                   string='Subordinates')
    active = fields.Boolean(string='Acive', default=True)

    # Medical Information
    allergic_towards = fields.Char(string='Allergic Towards')
    blood_group = fields.Many2one(comodel_name='blood.group', string='Blood Group')
    medical_insurance = fields.Char(string='Medical Insurance')

    # Personal Information
    date_of_birth = fields.Date(string='Date Of Birth')
    age = fields.Integer(string='Age', readonly=True)
    sex = fields.Selection([('male', 'Male'),
                            ('female', 'Female'),
                            ('transgender', 'Transgender')],
                           string='Sex')
    marital_status = fields.Selection([('married', 'married'),
                                       ('unmarried', 'Unmarried'),
                                       ('divorced', 'Divorced')],
                                      string='Marital Status')

    contact_address = fields.One2many(comodel_name='human.contact', inverse_name='hospital_employee_id',
                                      string='Contact Address')
    emergency_contact = fields.Many2one(comodel_name='human.contact', string='Emergency Contact')
    comments = fields.Text(string='Comments')

    # Professional Information
    education = fields.One2many(comodel_name='employee.education',
                                inverse_name='hospital_employee_id',
                                string='Education')
    experience = fields.One2many(comodel_name='employee.experience',
                                 inverse_name='hospital_employee_id',
                                 string='Experience')
    awards = fields.One2many(comodel_name='employee.awards',
                             inverse_name='hospital_employee_id',
                             string='Awards/Certification')

    # Programmatic
    status = fields.Selection([('draft', 'Draft'),
                               ('confirmed', 'Confirmed'),
                               ('exit', 'Exit')],
                              default='draft',
                              string='Status')

    # HR Information
    permission_approvar = fields.Many2one(comodel_name='hospital.employee', string='Permission Approvar')
    leave_approvar = fields.Many2one(comodel_name='hospital.employee', string='Leave Approvar')
    overtime_approvar = fields.Many2one(comodel_name='hospital.employee', string='Overtime Approvar')


Employee()



