# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class Product(models.Model):
    _name = 'product.product'
    _description = 'Product'
    _order = 'name'

    # Product
    name = fields.Char(string='Name', required=True)
    specification = fields.Text(string='Specification')
    product_group = fields.Many2one(comodel_name='product.groups', ondelete='cascade',
                                    required=True, string='Group')
    product_sub_group = fields.Many2one(comodel_name='product.subgroups', ondelete='cascade',
                                        required=True, string='Sub Group')
    average_price = fields.Float(string='Average Price',
                                 invisible="[('classification', '=', True)]")
    classification = fields.Boolean(string='Classify')
    uom = fields.Many2one(comodel_name='product.uom', ondelete='cascade',
                          required=True, string='UOM')

    parent_id = fields.Many2one(comodel_name='product.product', ondelete='cascade',
                                string='Sub-Product Of')
    child_ids = fields.One2many(comodel_name='product.product',
                                inverse_name='parent_id',
                                string='Product')
    hsn_code = fields.Char(string='HSN Code')
    code = fields.Char(string='Product Code')
    stock_id = fields.One2many(comodel_name='stock.stock',
                               inverse_name='product_id',
                               string='Stock')
    comments = fields.Text(string='Comments')

    sale_price = fields.One2many(comodel_name='product.sale.price',
                                 inverse_name='product_id',
                                 string='Sale Price')
    purchase_price = fields.One2many(comodel_name='product.purchase.price',
                                     inverse_name='product_id',
                                     string='Purchase Price')

    @api.onchange('classification')
    def onchange_classification(self):
        if not self.classification:
            recs = self.child_ids
            for rec in recs:
                rec.unlink()

    @api.multi
    def unlink(self):
        for rec in self:
            rec.active = False
        return super(Product, self).unlink()

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
        domain = ['|', '|', ('code', operator, name), ('name', operator, name), ('hsn_code', operator, name)]
        recs = self.search(domain + args, limit=limit)
        return recs.name_get()

    def create_sequence(self, product_group, product_sub_group):
        obj = self.env['ir.sequence'].sudo()

        sequence = obj.next_by_code('product.product')
        group_obj = self.env['product.groups'].sudo().search([('id', '=', product_group)])
        sub_group_obj = self.env['product.subgroups'].sudo().search([('id', '=', product_sub_group)])

        return '{0}/{1}/{2}'.format(group_obj.code, sub_group_obj.code, sequence)

    @api.model
    def create(self, vals):
        code = self.create_sequence(vals['product_group'], vals['product_sub_group'])
        vals['code'] = code
        rec = super(Product, self).create(vals)
        return rec


Product()





