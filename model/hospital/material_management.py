# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Assert(models.Model):
    _name = 'hospital.assert'

    name = fields.Char(string='Sequence', readonly=True)
    product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True)
    code = fields.Char(string='Code')
    comment = fields.Text(string='Comment')
    responsible_id = fields.Many2one(comodel_name='hospital.employee', string='Responsible Person')
    assert_id = fields.Many2one(comodel_name='hospital.assert', string='Assert')
    accessories_ids = fields.One2many(comodel_name='hospital.assert',
                                      inverse_name='assert_id',
                                      string='Accessories')
    purchase_date = fields.Date(string='Purchased Date')
    working = fields.Boolean(string='Working')
    warranty = fields.Char(string='Warranty')
    purchase_id = fields.Many2one(comodel_name='hospital.partner', string='Purchase')
    purchase_contact = fields.Char(string='Purchase Contact', related='purchase_id.phone')
    service_id = fields.Many2one(comodel_name='hospital.partner', string='Service')
    service_contact = fields.Char(string='Service Contact', related='purchase_id.phone')
    serial_no = fields.Char(string='Serial No')
    model_no = fields.Char(string='Model No')
    dimension = fields.Char(string='Dimension')
    operating_manual = fields.Binary(string='Operating Manual')
    documents = fields.Binary(string='Other Documents')
    service_ids = fields.One2many(comodel_name='assert.service',
                                  inverse_name='assert_id',
                                  string='Service')
    manufacturer = fields.Char(string='Manufacturer')
    location = fields.Many2one(comodel_name='hospital.location', string='Location')
    notification_ids = fields.One2many(comodel_name='assert.notification',
                                       inverse_name='assert_id',
                                       string='Notification')

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
    subject = fields.Char(string='Subject')
    email_to = fields.Char(string='Email To')
    email_cc = fields.Char(string='Email CC')
    assert_id = fields.Many2one(comodel_name='hospital.assert', string='Assert')


Notification()


