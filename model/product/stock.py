# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class Stock(models.Model):
    _name = 'stock.stock'

    product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True)
    location_id = fields.Many2one(comodel_name='stock.location', string='Location', required=True)
    quantity = fields.Float(string='Quantity')


Stock()
