# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class TimeDelayConfiguration(models.Model):
    _name = 'time.configuration'

    name = fields.Char(string='Name')
    time_delay = fields.Float(string='Time delay')


TimeDelayConfiguration()
