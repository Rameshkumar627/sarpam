# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions
from datetime import datetime, timedelta


class OrganisationalChart(models.AbstractModel):
    _name = 'report.sarpam.organisational_chart'

    @api.multi
    def render_html(self, docids, data=None):

        script = '''<script>
                    var config = {
        container: "#basic-example",
        
        connectors: {
            type: 'step'
        },
        node: {
            HTMLclass: 'nodeExample1'
        }
    },
        '''
        html = '''<!DOCTYPE html>
                <html>
                    <head>
                    <meta charset="utf-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
                    <meta name="viewport" content="width=device-width">
                    <title> Basic example </title>
                    <link rel="stylesheet" href="/sarpam/static/Treant.css">
                    <link rel="stylesheet" href="/sarpam/static/basic-example.css">
                    
                </head>
                <body>
                    <div class="chart" id="basic-example"></div>
                    <script src="/sarpam/static/raphael.js"></script>
                    <script src="/sarpam/static/Treant.js"></script>
                    
                    <script>
                    var config = {
        container: "#basic-example",
        
        connectors: {
            type: 'step'
        },
        node: {
            HTMLclass: 'nodeExample1'
        }
    },
    ceo = {
        text: {
            name: "Mark Hill",
            title: "Chief executive officer",
            contact: "Tel: 01 213 123 134",
        },
        image: "../headshots/2.jpg"
    },

    cto = {
        parent: ceo,
        text:{
            name: "Joe Linux",
            title: "Chief Technology Officer",
        },
        stackChildren: true,
        image: "../headshots/1.jpg"
    },
    cbo = {
        parent: ceo,
        stackChildren: true,
        text:{
            name: "Linda May",
            title: "Chief Business Officer",
        },
        image: "../headshots/5.jpg"
    },
    cdo = {
        parent: ceo,
        text:{
            name: "John Green",
            title: "Chief accounting officer",
            contact: "Tel: 01 213 123 134",
        },
        image: "../headshots/6.jpg"
    },
    cio = {
        parent: cto,
        text:{
            name: "Ron Blomquist",
            title: "Chief Information Security Officer"
        },
        image: "../headshots/8.jpg"
    },
    ciso = {
        parent: cto,
        text:{
            name: "Michael Rubin",
            title: "Chief Innovation Officer",
            contact: {val: "we@aregreat.com", href: "mailto:we@aregreat.com"}
        },
        image: "../headshots/9.jpg"
    },
    cio2 = {
        parent: cdo,
        text:{
            name: "Erica Reel",
            title: "Chief Customer Officer"
        },
        link: {
            href: "http://www.google.com"
        },
        image: "../headshots/10.jpg"
    },
    ciso2 = {
        parent: cbo,
        text:{
            name: "Alice Lopez",
            title: "Chief Communications Officer"
        },
        image: "../headshots/7.jpg"
    },
    ciso3 = {
        parent: cbo,
        text:{
            name: "Mary Johnson",
            title: "Chief Brand Officer"
        },
        image: "../headshots/4.jpg"
    },
    ciso4 = {
        parent: cbo,
        text:{
            name: "Kirk Douglas",
            title: "Chief Business Development Officer"
        },
        image: "../headshots/11.jpg"
    }
    riso4 = {
        parent: cto,
        text:{
            name: "Ramesh Kuamr",
            title: "Chief Business Development Officer"
        },
        image: "https://static.comicvine.com/uploads/scale_small/11/114183/5200279-links_image_4432.jpg"
    }

    chart_config = [
        config,
        ceo,
        cto,
        cbo,
        cdo,
        cio,
        ciso,
        cio2,
        ciso2,
        ciso3,
        ciso4,
	riso4
    ];


                    </script>
                    <script>
                        new Treant( chart_config );
                    </script>
                </body>
                </html>'''
        return html


OrganisationalChart()


class HospitalEmployeeChart(models.TransientModel):
    _name = 'hospital.employee.chart'

    @api.multi
    def print_report(self):

        obj = self.env['hospital.patient'].search([('id', '>', 0)])
        data = self.env['report'].get_action(obj, 'sarpam.organisational_chart', data=None)

        return data


HospitalEmployeeChart()


