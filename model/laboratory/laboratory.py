# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class Laboratory(models.Model):
    _name = 'laboratory.billing'

    sequence = fields.Char(string='Sequence')
    date = ''
    patient_id = ''
    patient_uid = ''
    lab_line_ids = ''
    comment = ''


Laboratory()


class LabLines(models.Model):
    _name = ''

    test_id = ''
    test_status = ''
    test_by = ''
    test_completed_on = ''
    test_report = ''
    test_line_ids = ''
    laboratory_id = ''
    comment = ''


LabLines()


class TestLine(models.Model):
    _name = ''

    name = ''
    result = ''
    comment = ''

TestLine()


