# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class BloodGroup(models.Model):
    _name = 'blood.group'

    name = fields.Char(string='Blood Group')


BloodGroup()
