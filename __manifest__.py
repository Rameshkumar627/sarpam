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
        'data/office.xml',
        'data/product.xml',
        'data/ledger.xml',
        'menu/menu.xml',
        'view/employee/hospital_employee.xml',
        'view/product/product_group.xml',
        'view/product/product_sub_group.xml',
        'view/product/product_uom.xml',
        'view/product/product_tax.xml',
        'view/product/product.xml',
        'view/product/stock.xml',
        'view/hospital/voucher.xml',
        'view/hospital/material_management.xml',
        'view/pharmacy/pharmacy.xml',
        'view/accounts/account_journal.xml',
        'view/accounts/account_ledger.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
