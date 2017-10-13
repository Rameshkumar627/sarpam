# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OrganisationalChart(models.AbstractModel):
    _name = 'report.sarpam.organisational_chart'

    @api.multi
    def render_html(self, docids, data=None):
        print "ramesh"
        data = '''
Result Size: 913 x 834
<!DOCTYPE html>

<html>

<head>

<style>

table {

    font-family: arial, sans-serif;

    border-collapse: collapse;

    width: 100%;

}

​

td, th {

    border: 1px solid #dddddd;

    text-align: left;

    padding: 8px;

}

​

tr:nth-child(even) {

    background-color: #dddddd;

}

</style>

</head>

<body>

​

<table>

  <tr>

    <th>Company</th>

    <th>Contact</th>

    <th>Country</th>

  </tr>

  <tr>

    <td>Alfreds Futterkiste</td>

    <td>Maria Anders</td>

    <td>Germany</td>

  </tr>

  <tr>

    <td>Centro comercial Moctezuma</td>

    <td>Francisco Chang</td>

    <td>Mexico</td>

  </tr>

  <tr>

    <td>Ernst Handel</td>

    <td>Roland Mendel</td>

    <td>Austria</td>

  </tr>

  <tr>

    <td>Island Trading</td>

    <td>Helen Bennett</td>

    <td>UK</td>

  </tr>

  <tr>

    <td>Laughing Bacchus Winecellars</td>

    <td>Yoshi Tannamuri</td>

    <td>Canada</td>

  </tr>

  <tr>

    <td>Magazzini Alimentari Riuniti</td>

    <td>Giovanni Rovelli</td>

    <td>Italy</td>

  </tr>

</table>

​

</body>

</html>

​

'''
        return data


OrganisationalChart()


class MakeChart(models.TransientModel):
    _name = 'make.chart'

    @api.multi
    def print_report(self):
        print "ramesh,,"
        obj = self.env['hospital.patient'].search([('id', '>', 0)])
        data = self.env['report'].get_action(obj, 'sarpam.organisational_chart', data=None)
        print data
        return data

MakeChart()


