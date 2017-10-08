# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Bank(models.Model):
    _name = 'account.bank'

    name = fields.Char(string='Bank name')


Bank()
