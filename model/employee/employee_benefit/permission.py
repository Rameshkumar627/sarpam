# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _
from datetime import datetime, timedelta


class Permission(models.Model):
    _name = 'employee.permission'

    date = fields.Date(string='Date', required=True)
    employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee', required=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('approved', 'Approved'),
                              ('cancelled', 'Cancelled')],
                             default='draft',
                             string='State')
    hours = fields.Float(string='Hours', required=True)
    reason = fields.Text(string='Reason', required=True)
    approved_by = fields.Many2one(comodel_name='hospital.employee', string='Approved By', readonly=True)
    approved_on = fields.Date(string='Approved On', readonly=True)
    comment = fields.Text(string='Comment')
    app_notification = fields.Text(string='Notification')

    def get_grant_access_group_status(self):
        for rec in self:
            if rec.state == 'draft':
                rec.grant_access_group = rec.get_current_user_group(['Hospital Employee'])
            elif rec.state == 'confirmed':
                rec.grant_access_group = rec.get_current_user_group(['Hospital HR'])

    def get_current_user_group(self, groups):
        group_ids = self.env.user.groups_id
        status = False
        for group in group_ids:
            if group.name in groups:
                status = True
        return status

    def check_rights(self):
        if not self.get_grant_access_group_status():
            raise exceptions.ValidationError('Error! You are not have access')

    @api.multi
    def confirm_button(self):
        self.check_rights()
        self.write({'state': 'confirmed'})

        self.app_notification = "Your Permission Application in send for approval"
        data = {
            'name': _('Leave Application'),
            'view_mode': 'form',
            'view_id': self.env.ref('sarpam.view_employee_leave_application_notification_form').id,
            'res_model': 'employee.leave.application',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'new'
        }

        return data

    @api.multi
    def approve_button(self):
        self.check_rights()
        data = {'state': 'approved',
                'approved_on': datetime.now().strftime("%Y-%m-%d"),
                'approved_by': self.env.user.id}
        self.write(data)

        self.app_notification = "{0} Permission application is approved".format(self.employee_id.name)
        data = {
            'name': _('Leave Application'),
            'view_mode': 'form',
            'view_id': self.env.ref('sarpam.view_employee_leave_application_notification_form').id,
            'res_model': 'employee.leave.application',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'new'
        }

        return data

    @api.multi
    def cancel_button(self):
        self.check_rights()
        self.write({'state': 'cancelled'})

    @api.multi
    def unlink(self):
        raise exceptions.ValidationError("Error! You are not having access to delete this record")

Permission()


class Overtime(models.Model):
    _name = 'employee.overtime'

    date = fields.Date(string='Date', required=True)
    employee_id = fields.Many2one(comodel_name='hospital.employee', string='Employee', required=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('approved', 'Approved'),
                              ('cancelled', 'Cancelled')],
                             default='draft',
                             string='State')
    hours = fields.Float(string='Hours', required=True)
    reason = fields.Text(string='Reason', required=True)
    approved_by = fields.Many2one(comodel_name='hospital.employee', string='Approved By', readonly=True)
    approved_on = fields.Date(string='Approved On', readonly=True)
    comment = fields.Text(string='Comment')

    def get_grant_access_group_status(self):
        for rec in self:
            if rec.state == 'draft':
                rec.grant_access_group = rec.get_current_user_group(['Hospital Employee'])
            elif rec.state == 'confirmed':
                rec.grant_access_group = rec.get_current_user_group(['Hospital HR'])

    def get_current_user_group(self, groups):
        group_ids = self.env.user.groups_id
        status = False
        for group in group_ids:
            if group.name in groups:
                status = True
        return status

    def check_rights(self):
        if not self.get_grant_access_group_status():
            raise exceptions.ValidationError('Error! You are not have access')

    @api.multi
    def confirm_button(self):
        self.check_rights()
        self.write({'state': 'confirmed'})

        self.app_notification = "Your Over-Time Application in send for approval"
        data = {
            'name': _('Leave Application'),
            'view_mode': 'form',
            'view_id': self.env.ref('sarpam.view_employee_leave_application_notification_form').id,
            'res_model': 'employee.leave.application',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'new'
        }

        return data

    @api.multi
    def approve_button(self):
        self.check_rights()
        data = {'state': 'approved',
                'approved_on': datetime.now().strftime("%Y-%m-%d"),
                'approved_by': self.env.user.id}
        self.write(data)

        self.app_notification = "{0} Over-Time application is approved".format(self.employee_id.name)
        data = {
            'name': _('Leave Application'),
            'view_mode': 'form',
            'view_id': self.env.ref('sarpam.view_employee_leave_application_notification_form').id,
            'res_model': 'employee.leave.application',
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            'target': 'new'
        }

        return data

    @api.multi
    def cancel_button(self):
        self.check_rights()
        self.write({'state': 'cancelled'})

    @api.multi
    def unlink(self):
        raise exceptions.ValidationError("Error! You are not having access to delete this record")

Overtime()


