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
        'view/office/awards.xml',
        'view/office/bank.xml',
        'view/office/blood_group.xml',
        'view/office/contact.xml',
        'view/office/country.xml',
        'view/office/course.xml',
        'view/office/education.xml',
        'view/office/employee_type.xml',
        'view/office/hospital_location.xml',
        'view/office/partner.xml',
        'view/office/state.xml',
        'view/office/stock_location.xml',
        'view/patient/patient.xml',
        'view/patient/appointment.xml',
        'view/patient/out_patient.xml',
        'view/hospital/voucher.xml',
        'view/hospital/material_management.xml',
        'view/pharmacy/pharmacy.xml',
        'view/accounts/account_journal.xml',
        'view/accounts/account_ledger.xml',
        'view/contact/contact.xml',
        'view/employee/hospital_employee.xml',
        'view/employee/organisational_chart.xml',
        'view/employee/employee_benefit/leave_application.xml',
        'view/employee/employee_benefit/permission.xml',
        'view/employee/employee_benefit/overtime.xml',
        'view/employee/time/shift.xml',
        'view/employee/time/time_schedule.xml',
        'view/employee/time/time_sheet.xml',
        'view/employee/time/attendance.xml',
        'view/employee/time/employee_timesheet.xml',
        'view/employee/time_configuration.xml',
        'view/employee/time/attendance_report.xml',
        'view/employee/payroll/pay_slip.xml',
        'view/employee/payroll/pay_slip_data.xml',
        'view/employee/payroll/batches.xml',
        'view/employee/payroll/salary_rule.xml',
        'view/employee/payroll/salary_structure.xml',
        'view/employee/payroll/wages.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
