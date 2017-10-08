# -*- coding: utf-8 -GPK*-

{
    'name': 'Hospital',
    'version': '1.0',
    'author': 'Yali Technologies',
    'category': 'Hostial ERP',
    'sequence': 1,
    'website': 'www.yalitechnologies.com',
    'depends': ['base', 'board', 'mail'],
    'data': [
        'data/employee.xml',
        'menu/menu.xml',
        'view/employee/hospital_employee.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
