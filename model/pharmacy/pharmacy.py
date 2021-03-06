# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Pharmacy(models.Model):
    _name = 'hospital.pharmacy'

    name = fields.Char(string='Sequence', readonly=True)
    date = fields.Date(string='Date', required=True)
    customer_id = fields.Many2one(comodel_name='hospital.partner', string='Customer', required=True)
    phone = fields.Char(string='Phone', related='customer_id.phone')
    email = fields.Char(string='Email', related='customer_id.email')
    total = fields.Float(string='Total', readonly=True)
    cgst = fields.Float(string='CGST', readonly=True)
    sgst = fields.Float(string='SGST', readonly=True)
    round_off = fields.Float(string='Round Off', readonly=True)
    discount = fields.Float(string='Discount', readonly=True)
    packing_forwading = fields.Float(string='Packaging & Forwading')
    comment = fields.Text(string='Comment')
    pharmacy_line_ids = fields.One2many(comodel_name='hospital.pharmacy.line',
                                        inverse_name='pharmacy_id',
                                        string='Pharmacy Lines')
    state = fields.Selection([('draft', 'Draft'), ('payment_made', 'Payment Made')],
                             default='draft',
                             string='State')
    account = fields.Selection([('bank', 'Bank'), ('cash', 'Cash')], string='Account')
    restrict_journal = fields.Boolean(string='Restrict Journal', default=False)

    def get_current_user_group(self, groups):
        group_ids = self.env.user.groups_id
        status = False
        for group in group_ids:
            if group.name in groups:
                status = True
        return status

    def check_rights(self):
        for rec in self:
            if rec.state == 'draft':
                rec.grant_access_group = rec.get_current_user_group(['Hospital - Administrator',
                                                                     'Hospital - Pharmacist'])

    def get_sequence(self):
        obj = self.env['ir.sequence'].sudo()
        sequence = obj.next_by_code('hospital.pharmacy')
        period = self.env['period.period'].search([('state', '=', 'open')])
        return '{0}/{1}'.format(sequence, period.name)

    def update_total(self):
        total = tax_amount = 0
        recs = self.pharmacy_line_ids

        for rec in recs:
            rec.update_total()
            total = total + rec.total
            tax_amount = tax_amount + rec.tax_amount

        if not total:
            raise exceptions.ValidationError('Error! Require amount for further progress')

        return total, tax_amount

    def update_account_journal(self):
        if self.restrict_journal:
            raise exceptions.ValidationError('Error! Journal Entries already done')

        journal_data = {}
        journal = self.env['hospital.account.journal'].sudo()

        journal_data['reference'] = self.name
        rec = journal.create(journal_data)

        # Ledger For Pharmacy

        # Amount In Pharmacy journal
        data = {}
        ledger = self.env['hospital.account.ledger'].search([('name', '=', 'Pharmacy Ledger')])
        data['ledger_id'] = ledger.id
        data['journal_id'] = rec.id
        data['reference'] = self.name
        data['description'] = 'From Pharmacy'
        data['credit'] = 0
        data['debit'] = self.total

        rec.journal_line_ids.create(data)
        # Amount Split to Tax journal and Cash journal
        # Tax Journal
        data = {}
        ledger = self.env['hospital.account.ledger'].search([('name', '=', 'Tax Ledger')])
        data['ledger_id'] = ledger.id
        data['journal_id'] = rec.id
        data['reference'] = self.name
        data['description'] = 'To Tax'
        data['credit'] = self.cgst + self.sgst
        data['debit'] = 0

        rec.journal_line_ids.create(data)
        if self.account == 'cash':
            # Cash Journal
            data = {}
            ledger = self.env['hospital.account.ledger'].search([('name', '=', 'Cash Ledger')])
            data['ledger_id'] = ledger.id
            data['journal_id'] = rec.id
            data['reference'] = self.name
            data['description'] = 'To Cash'
            data['credit'] = self.total
            data['debit'] = 0

            rec.journal_line_ids.create(data)

        if self.account == 'bank':
            # Bank Journal
            data = {}
            ledger = self.env['hospital.account.ledger'].search([('name', '=', 'Bank Ledger')])
            data['ledger_id'] = ledger.id
            data['journal_id'] = rec.id
            data['reference'] = self.name
            data['description'] = 'To Bank'
            data['credit'] = self.total
            data['debit'] = 0

        rec.journal_line_ids.create(data)
        self.write({'restrict_journal': True})

    def stock_updation(self):
        pass

    @api.multi
    def payment_made_button(self):
        data = {}
        self.check_rights()
        self.stock_updation()
        sequence = self.get_sequence()
        total, tax_amount = self.update_total()
        discount = total * float(self.discount / 100)

        discounted_total = total - discount
        packing_forwading = discounted_total * float(self.packing_forwading / 100)
        total = discounted_total + packing_forwading
        round_off = total - round(total)

        data['cgst'] = tax_amount / 2
        data['sgst'] = tax_amount / 2
        data['state'] = 'payment_made'
        data['name'] = sequence
        data['round_off'] = round_off
        data['total'] = total - round_off
        data['packing_forwading'] = packing_forwading
        data['discount'] = discount
        self.write(data)

        self.update_account_journal()


Pharmacy()


class PharmacyLine(models.Model):
    _name = 'hospital.pharmacy.line'

    product_id = fields.Many2one(comodel_name='product.product', string='Product', required=True)
    uom_id = fields.Many2one(comodel_name='product.uom', string='UOM', required=True)
    tax_id = fields.Many2one(comodel_name='product.tax', string='Tax', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    unit_price = fields.Float(string='Unit Price', required=True)
    discount = fields.Float(string='Discount')
    total = fields.Float(string='Total', required=True)
    tax_amount = fields.Float(string='Tax Amount')
    pharmacy_id = fields.Many2one(comodel_name='hospital.pharmacy', string='Pharmacy')

    def update_total(self):
        data = {}

        price = self.quantity * self.unit_price
        discounted_price = price + (price * float(self.discount / 100))
        tax_amount = discounted_price * float(self.tax_id.rate / 100)
        total = discounted_price + tax_amount

        data['total'] = total
        data['tax_amount'] = tax_amount

        self.write(data)


PharmacyLine()
