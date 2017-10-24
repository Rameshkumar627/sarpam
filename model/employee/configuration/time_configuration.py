# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class TimeDelayConfiguration(models.Model):
    _name = 'time.configuration'

    name = fields.Char(string='Name')
    half_day = fields.Float(string='Half Day')
    full_day = fields.Float(string='Full Day')


TimeDelayConfiguration()
