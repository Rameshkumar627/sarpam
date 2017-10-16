# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta
import math


class Shift(models.Model):
    _name = 'employee.shift'

    name = fields.Char(string='Shift', required=True)
    from_time_hours = fields.Integer(string='From Hours', required=True)
    from_time_min = fields.Integer(string='From Min', required=True)
    till_time_hours = fields.Integer(string='Till Hours', readonly=True)
    till_time_min = fields.Integer(string='Till Min', readonly=True)
    duration = fields.Float(string='Duration', reaquired=True)
    comment = fields.Text(string='Comment')

    @api.multi
    def calc_till_button(self):
        data = {}
        end_time = float(self.from_time_hours) + (float(self.from_time_min)/100) + float(self.duration)
        mins, hours = math.modf(end_time)

        if hours > 24:
            hours = hours - 24
        data['till_time_hours'] = hours
        data['till_time_min'] = mins * 100 + 1
        self.write(data)


Shift()
