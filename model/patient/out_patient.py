# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OutPatient(models.Model):
    _name = 'out.patient'

    sequence = fields.Char(string='Sequence')
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    patient_uid = fields.Char(string='Patient ID', related='patient_id.patient_uid')
    age = fields.Integer(string='Age', related='patient_id.age')
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    symptom_ids = fields.Many2many(comodel_name='symptoms.symptoms', string='Symptoms')
    diagnosis_ids = fields.Many2many(comodel_name='diagnosis.diagnosis', string='Diagnosis')
    treatment = fields.Text(string='Treatment')
    scan = fields.Boolean(string='Scan')
    test = fields.Boolean(string='Test')
    medicine_suggestion_ids = fields.One2many(comodel_name='pharmacy.medicine',
                                              inverse_name='out_patient_id',
                                              string='Medicine')
    scan_suggestion_ids = fields.Many2many(comodel_name='laboratory.scan',
                                           string='Scan')
    test_suggestion_ids = fields.Many2many(comodel_name='laboratory.test',
                                           string='Test')
    report_html = fields.Html(string='Report', readonly=True)
    comment = fields.Text(string='Comment')
    next_appointment = fields.Datetime(string='Next Appointment')
    state = fields.Selection([('open', 'Open'), ('closed', 'Closed')], default='open', string='State')

    def get_sequence(self):
        obj = self.env['ir.sequence'].sudo()
        sequence = obj.next_by_code('out.patient')
        period = self.env['period.period'].search([('state', '=', 'open')])
        return '{0}/{1}'.format(sequence, period.name)

    @api.multi
    def update_suggestion(self):
        '''Update suggested medicine/scan/test by selecting diagnosis'''
        pass

    @api.multi
    def generate_report_action(self):
        '''Create HTML report for the patient'''
        pass

    @api.multi
    def close_action(self):
        self.generate_report_action()

        data = {'state': 'closed',
                'sequence': self.get_sequence()}

        self.write(data)


OutPatient()


