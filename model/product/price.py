# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class PurchasePrice(models.Model):
    _name = 'product.purchase.price'
    _description = 'Price'
    _order = 'name'

    # Product
    name = fields.Date(string='Date', required=True)
    purchase_price = fields.Float(string='Purchase Price')
    ref = fields.Char(string='Purchase Reference')
    product_id = fields.Many2one(comodel_name='product.product', string='Product', ondelete='cascade')


PurchasePrice()


class SalePrice(models.Model):
    _name = 'product.sale.price'
    _description = 'Price'
    _order = 'name'

    # Product
    name = fields.Date(string='Date', required=True)
    sale_price = fields.Float(string='Sale Price')
    product_id = fields.Many2one(comodel_name='product.product', string='Product', ondelete='cascade')


SalePrice()
