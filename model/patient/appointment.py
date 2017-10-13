# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Appointment(models.Model):
    _name = 'hospital.appointment'

    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='patient', required=True)
    patient_uid = fields.Char(string='ID')
    staff = fields.Many2one(comodel_name='hospital.employee', string='Doctor/ Staff')
    reason = fields.Text(string='Reason', required=True)
    comment = fields.Text(string='Comment')

    @api.multi
    def sms_initmate(self):
        pass

    @api.multi
    def mail_intimate(self):
        pass


Appointment()



