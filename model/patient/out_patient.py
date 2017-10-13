# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OutPatient(models.Model):
    _name = 'out.patient'

    sequence = fields.Char(string='Sequence')
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    patient_uid = fields.Char(string='ID', related='patient_id.patient_uid')
    age = fields.Integer(string='Age', related='patient_id.age')
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
    symptom_ids = fields.Many2many(comodel_name='symptoms.symptoms', string='Symptoms')
    diagnosis_ids = fields.One2many(comodel_name='patient.diagnosis', inverse_name='patient_id', string='Diagnosis')
    treatment = fields.Text(string='Treatment')
    medicine = fields.Boolean(string='Medicine')
    scan = fields.Boolean(string='Scan')
    test = fields.Boolean(string='Test')
    medicine_suggestion_ids = fields.One2many(comodel_name='medicine.suggestion',
                                              inverse_name='patient_id',
                                              string='Medicine')
    scan_suggestion_ids = fields.One2many(comodel_name='scan.suggestion',
                                          inverse_name='patient_id',
                                          string='Scan')
    test_suggestion_ids = fields.One2many(comodel_name='test.suggestion',
                                          inverse_name='patient_id',
                                          string='Test')
    report_html = fields.Html(string='Report', readonly=True)
    comment = fields.Text(string='Comment')
    next_appointment = fields.Datetime(string='Next Appointment')

    @api.multi
    def update_suggestion(self):
        pass


OutPatient()


class PatientDiagnosis(models.Model):
    _name = 'patient.diagnosis'

    name = fields.Many2one(comodel_name='diagnosis.diagnosis', string='Diagnosis')
    comment = fields.Text(string='Comment')
    patient_id = fields.Many2one(comodel_name='out.patient', string='Out Patient')


PatientDiagnosis()


class MedicineSuggestion(models.Model):
    _name = 'medicine.suggestion'

    medicine_id = fields.Many2one(comodel_name='product.product', string='Medicine')
    select = fields.Boolean(string='Select')
    patient_id = fields.Many2one(comodel_name='out.patient', string='Out Patient')


MedicineSuggestion()


class ScanSuggestion(models.Model):
    _name = 'scan.suggestion'

    scan_id = fields.Many2one(comodel_name='scan.scan', string='Scan')
    select = fields.Boolean(string='Select')
    patient_id = fields.Many2one(comodel_name='out.patient', string='Out Patient')


ScanSuggestion()


class TestSuggestion(models.Model):
    _name = 'test.suggestion'

    test_id = fields.Many2one(comodel_name='test.test', string='Test')
    select = fields.Boolean(string='Select')
    patient_id = fields.Many2one(comodel_name='out.patient', string='Out Patient')


TestSuggestion()
