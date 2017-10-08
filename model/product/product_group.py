# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class ProductGroups(models.Model):
    _name = 'product.groups'
    _description = 'Product Groups'

    name = fields.Char(string='Group', required=True)
    code = fields.Char(string='Group Code', required=True)
    active = fields.Boolean(string='Active', default=True)

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.name:
                name = "[{0}] - {1}".format(record.code, record.name)
                result.append((record.id, name))
        return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=80):
        args = args or []
        domain = ['|', ('code', operator, name), ('name', operator, name)]
        recs = self.search(domain + args, limit=limit)
        return recs.name_get()

    @api.multi
    def unlink(self):
        for rec in self:
            rec.active = False
        return super(ProductGroups, self).unlink()


ProductGroups()
