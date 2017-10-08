# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class Tax(models.Model):
    _name = 'product.tax'
    _description = 'Tax'
    _order = 'name'

    name = fields.Char(string='Tax', required=True)
    rate = fields.Float(string='Rate (%)', required=True)

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.name:
                name = "[{0}] - {1}%".format(record.name, record.rate)
                result.append((record.id, name))
        return result

    @api.multi
    def unlink(self):
        for rec in self:
            rec.active = False
        return super(Tax, self).unlink()

Tax()
