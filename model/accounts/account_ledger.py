# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Ledger(models.Model):
    _name = 'hospital.account.ledger'

    name = fields.Char(string='Name', readonly=True)
    comment = fields.Text(string='Comment')
    ledger_line_ids = fields.One2many(comodel_name='hospital.account.journal.line',
                                      inverse_name='ledger_id',
                                      string='Ledger Lines')


Ledger()
