# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class InPatient(models.Model):
    _name = 'in.patient'

    sequence = fields.Char(string='Sequence')
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    patient_uid = fields.Char(string='ID', related='patient_id.patient_uid')
    treatment_ids = fields.One2many(comodel_name='in.patient.treatment',
                                    inverse_name='in_patient_id',
                                    string='Treatment')
    ward_ids = fields.One2many(comodel_name='in.patient.ward',
                               inverse_name='in_patient_id',
                               string='Ward')
    todo_ids = fields.One2many(comodel_name='in.patient.todo',
                               inverse_name='in_patient_id',
                               string='Todo')
    admission_detail = fields.Text(string='Admission Detail')
    date = fields.Datetime(string='Date')


InPatient()


class InPatientTreatment(models.Model):
    _name = 'in.patient.treatment'

    date = fields.Datetime(string='Date')
    treated_by = fields.Many2one(comodel_name='hospital.patient', string='Treated By')
    treatment = fields.Text(string='Treatment')
    comment = fields.Text(string='Comment')
    in_patient_id = fields.Many2one(comodel_name='in.patient', string='In Patient')


InPatientTreatment()


class InPatientWard(models.Model):
    _name = 'in.patient.ward'

    from_date = fields.Datetime(string='From Date')
    till_date = fields.Datetime(string='Till Date')
    ward = fields.Many2one(comodel_name='hospital.ward', string='Ward')
    comment = fields.Text(string='Comment')
    in_patient_id = fields.Many2one(comodel_name='in.patient', string='In Patient')


InPatientWard()


class InPatientTodo(models.Model):
    _name = 'in.patient.todo'

    date = fields.Datetime(string='Date')
    notification_to = fields.Many2one(comodel_name='hospital.employee', string='To')
    notification = fields.Char(string='Notification')
    comment = fields.Text(string='Comment')
    in_patient_id = fields.Many2one(comodel_name='in.patient', string='In Patient')


InPatientTodo()
