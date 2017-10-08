# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Contact(models.Model):
    _name = 'human.contact'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    state = fields.Many2one(comodel_name='human.state', string='State')
    country = fields.Many2one(comodel_name='human.country', string='Country')
    pincode = fields.Char(string='Pincode')
    comment = fields.Char(string='Comment')
    hospital_employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee')


Contact()


class Country(models.Model):
    _name = 'human.country'

    name = fields.Char(string='Country')


Country()


class State(models.Model):
    _name = 'human.state'

    name = fields.Char(string='state')
    country = fields.Many2one(comodel_name='human.country', string='Country')


State()
