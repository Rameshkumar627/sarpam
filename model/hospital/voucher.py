# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Voucher(models.Model):
    _name = 'hospital.voucher'

    name = fields.Char(string='Sequence', readonly=True)
    employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee', required=True)
    employee_uid = fields.Char(string='Employee ID', related='employee_id.employee_uid')
    date = fields.Date(string='Date', required=True)
    total = fields.Float(string='Total', readonly=True)
    voucher_line_ids = fields.One2many(comodel_name='hospital.voucher.line',
                                       inverse_name='voucher_id',
                                       string='Voucher Lines')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'confirmed')],
                             default='draft',
                             string='State')

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
                                                                     'Hospital - Accounts'])

    def get_sequence(self):
        obj = self.env['ir.sequence'].sudo()
        sequence = obj.next_by_code('hospital.voucher')
        period = self.env['period.period'].search([('state', '=', 'open')])
        return '{0}/{1}'.format(sequence, period.name)

    def update_total(self):
        total = 0
        recs = self.voucher_line_ids

        for rec in recs:
            total = total + rec.amount

        if not total:
            raise exceptions.ValidationError('Error! Require amount for further progress')

        return total

    def update_account_journal(self):
        pass

    @api.multi
    def confirm_button(self):
        data = {}
        self.check_rights()
        sequence = self.get_sequence()
        total = self.update_total()

        data['total'] = total
        data['state'] = 'confirmed'
        data['name'] = sequence
        self.write(data)

        self.update_account_journal()

Voucher()


class VoucherLine(models.Model):
    _name = 'hospital.voucher.line'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    amount = fields.Float(string='Amount', required=True)
    voucher_id = fields.Many2one(comodel_name='hospital.voucher', string='Voucher')


VoucherLine()
