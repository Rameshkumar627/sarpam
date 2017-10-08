# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class ProductUOM(models.Model):
    _name = 'product.uom'
    _description = 'Product UOM'
    _order = 'name'

    name = fields.Char(string='Short Name', required=True)
    full_name = fields.Char(string='Full Name')


ProductUOM()
