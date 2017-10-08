# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Period(models.Model):

    _name = 'period.period'
    _rec_name = 'name'

    name = fields.Many2one(comodel_name='account.month', string='Period', required=True)
    code = fields.Char(string='Period', readonly=True)

    state = fields.Selection([('draft', 'Draft'),
                              ('open', 'Open'),
                              ('closed', 'Closed')],
                             default='draft')

    def check_state(self):
        recs = self.env['period.period'].search([('state', '=', 'open')])
        if recs:
            raise exceptions.ValidationError('Error! Close all period before open this period')

    @api.multi
    def action_open(self):
        self.check_state()
        self.get_period()
        self.state = 'open'

    @api.multi
    def action_close(self):
        self.update_store_request_sequence()
        self.state = 'closed'

    def update_store_request_sequence(self):
        models = ['hospital.voucher']

        for model in models:
            recs = self.env['ir.sequence'].search([('code', 'like', model)])
            for rec in recs:
                rec.write({'number_next_actual': 1})

    def get_period(self):
        if self.name:
            date = datetime.strptime(self.name.from_date, '%Y-%m-%d')
            month = int(date.strftime('%m'))
            if month > 3:
                current_year = int(date.strftime('%y'))
            else:
                current_year = int(date.strftime('%y')) - 1

            next_year = current_year + 1
            self.code = '{0}-{1}'.format(current_year, next_year)


Period()
