# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class HospitalLocation(models.Model):
    _name = 'hospital.location'

    name = fields.Char(string='Hospital Location')


HospitalLocation()


class StockLocation(models.Model):
    _name = 'stock.location'

    name = fields.Char(string='Stock Location')


StockLocation()


