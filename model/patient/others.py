# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Symptoms(models.Model):
    _name = 'symptoms.symptoms'

    name = fields.Char(string='Symptoms')
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
    comment = fields.Text(string='Comment')


Symptoms()


class Diagnosis(models.Model):
    _name = 'diagnosis.diagnosis'

    name = fields.Char(string='Diagnosis')


Diagnosis()
