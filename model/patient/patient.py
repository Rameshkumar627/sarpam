# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Patient(models.Model):
    _name = 'hospital.patient'

    image = fields.Binary(string='Image')
    name = fields.Char(string='Name')
    patient_uid = fields.Char(string='ID')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
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

    contact_address = fields.One2many(comodel_name='human.contact',
                                      inverse_name='hospital_patient_id',
                                      string='Contact Address')
    emergency_contact = fields.Many2one(comodel_name='human.contact', string='Emergency Contact')
    comments = fields.Text(string='Comments')


Patient()
