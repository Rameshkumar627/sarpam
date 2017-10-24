# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Symptoms(models.Model):
    _name = 'symptoms.symptoms'

    name = fields.Char(string='Symptoms')
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
    comment = fields.Text(string='Comment')


Symptoms()


class Diagnosis(models.Model):
    _name = 'diagnosis.diagnosis'

    name = fields.Char(string='Diagnosis')
    scan_ids = fields.Many2many(comodel_name='laboratory.scan', string='Scan')
    medicine_ids = fields.Many2many(comodel_name='product.product', string='Medicine')
    test_ids = fields.Many2many(comodel_name='laboratory.test', string='Test')


Diagnosis()


class PharmacyMedicine(models.Model):
    _name = 'pharmacy.medicine'

    name = fields.Many2one(comodel_name='product.product', string='Medicine')
    morning = fields.Boolean(string='AM')
    afternoon = fields.Boolean(string='NOON')
    evening = fields.Boolean(string='PM')
    days = fields.Integer(string='Days')
    out_patient_id = fields.Many2one(comodel_name='out.patient', string='Out Patient')


PharmacyMedicine()


class LaboratoryScan(models.Model):
    _name = 'laboratory.scan'

    name = fields.Char(string='Scan')


LaboratoryScan()


class LaboratoryTest(models.Model):
    _name = 'laboratory.test'

    name = fields.Char(string='Test')


LaboratoryTest()

