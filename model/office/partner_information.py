# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Partner(models.Model):
    _name = 'hospital.partner'

    name = fields.Char(string='Name')
    partner_ref = fields.Char(string='ID')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    bank_name = fields.Many2one(comodel_name='account.bank', string='Bank')
    account_no = fields.Char(string='Bank Account No')
    pan = fields.Char(string='PAN', required=True)
    aadhar_card = fields.Char(string='Aadhar Card')
    active = fields.Boolean(string='Active', default=True)
    office_address = fields.Many2one(comodel_name='human.contact', string='Office Address')
    contact_address = fields.One2many(comodel_name='human.contact',
                                      inverse_name='hospital_employee_id',
                                      string='Contact Address')

Partner()
