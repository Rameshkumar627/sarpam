# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class ProductSubGroups(models.Model):
    _name = 'product.subgroups'
    _description = 'Product Sub-Groups'

    name = fields.Char(string='Sub Group', required=True)
    code = fields.Char(string='Sub Group Code', required=True)
    active = fields.Boolean(string='Active', default=True)
    product_group = fields.Many2one(comodel_name='product.groups', ondelete='cascade', string='Group', required=True)

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
        return super(ProductSubGroups, self).unlink()

ProductSubGroups()
