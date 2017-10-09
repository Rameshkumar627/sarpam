# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Journal(models.Model):
    _name = 'hospital.account.journal'

    name = fields.Char(string='Sequence', readonly=True)
    date = fields.Date(string='Date', readonly=True)
    reference = fields.Char(string='Reference', readonly=True)
    comment = fields.Text(string='Comment')
    journal_line_ids = fields.One2many(comodel_name='hospital.account.journal.line',
                                       inverse_name='journal_id',
                                       string='Journal Lines')

    def get_sequence(self):
        obj = self.env['ir.sequence'].sudo()
        sequence = obj.next_by_code('hospital.account.journal')
        period = self.env['period.period'].search([('state', '=', 'open')])
        return '{0}/{1}'.format(sequence, period.name)

    def update_vals(self, vals):
        vals['date'] = datetime.now().strftime('%Y-%m-%d')
        vals['name'] = self.get_sequence()
        return vals

    @api.model
    def create(self, vals):
        vals = self.update_vals(vals)
        rec = super(Journal, self).create(vals)
        return rec

Journal()


class JournalLine(models.Model):
    _name = 'hospital.account.journal.line'

    ledger_id = fields.Many2one(comodel_name='hospital.account.ledger',
                                string='Ledger', readonly=True)
    journal_id = fields.Many2one(comodel_name='hospital.account.journal',
                                 string='Journal', readonly=True)
    reference = fields.Char(string='Reference', readonly=True)
    description = fields.Text(string='Description', readonly=True)
    credit = fields.Float(string='Credit', readonly=True)
    debit = fields.Float(string='Debit', readonly=True)


JournalLine()
