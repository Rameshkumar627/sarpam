# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Assert(models.Model):
    _name = 'hospital.assert'

    name = fields.Char(string='Sequence', readonly=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product')
    code = fields.Char(string='Code')
    comment = fields.Text(string='Comment')
    responsible_id = fields.Many2one(comodel_name='hospital.employee', string='Responsible Person')
    accessories_ids = fields.One2many(comodel_name='hospital.assert', string='Accessories')
    purchase_date = fields.Date(string='Purchased Date')
    status = fields.Selection()
    warranty = fields.Char(string='Warranty')
    purchase_contact = fields.Many2one(comodel_name='')
    service_contact = fields.Many2one(comodel_name='')
    serial_no = fields.Char(string='Serial No')
    model_no = fields.Char(string='Serial No')
    dimension = fields.Char(string='Serial No')
    operating_manual = fields.Binary(string='Operating Manual')
    documents = fields.Binary(string='Other Documents')
    service_ids = ''
    manufacturer = fields.Char(string='Serial No')
    location = fields.Many2one(comodel_name='hospital.location', string='Location')
    notification_id = ''


Assert()


class Service(models.Model):
    _name = 'assert.service'

    date = fields.Date(string='Date')
    description = fields.Text(string='Description')
    amount = fields.Float(string='Amount')
    documents = fields.Binary(string='Documents')
    assert_id = fields.Many2one(comodel_name='hospital.assert', string='Assert')


Service()


class Notification(models.Model):
    _name = 'assert.notification'

    date = fields.Date(string='Date')
    description = fields.Html(string='Description')
    email_to = fields.Char(string='Email To')
    email_cc = fields.Char(string='Email CC')


Notification()


