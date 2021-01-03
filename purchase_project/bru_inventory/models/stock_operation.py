# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

from datetime import datetime, timedelta, date


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    year_budget_id = fields.Selection(

        selection=[
            ('2560', '2560'),
            ('2561', '2561'),
            ('2562', '2562'),
            ('2563', '2563'),
            ('2564', '2564'),
            ('2565', '2565'),
            ('2566', '2566'),
            ('2567', '2567'),
            ('2568', '2568'),
            ('2569', '2569'),
            ('2570', '2570')
        ],
        # related='purchase_id.year_budget_id',
        string='ปีงบประมาณ'
    )
    document_type = fields.Selection(

        selection=[
            ('PR01', u'PR01=ขออนุมัติซื้อวัสดุ'),
            ('PR02', u'PR02=ขออนุมัติซื้อครุภัณฑ์'),
            ('PR03', u'PR03=ขออนุมัติจัดจ้าง')
        ],

        # related='purchase_id.document_type',
        string='ประเภทเอกสาร'
    )
    name = fields.Many2one(
        'res.partner',
        string='เจ้าหน้าที่พัสดุ',
        # oldname='name'
        # related='purchase_id.name'
    )
    bru_officer_id = fields.Many2one(
        'bru.branch',
        string='ชื่อหน่วยงาน',
        # oldname='bru_officer_id'
        # related='purchase_id.bru_officer_id'
    )
    for_use = fields.Char(
        string='เพื่อใช้ในงานราชการ',
        # oldname='for_use'
        # related='purchase_id.for_use'
    )
    budget_id = fields.Many2one(
        'bru.budget',
        string='งบประมาณ',
        # oldname='budget_id'
        # related='purchase_id.budget_id'
    )
    purchase_number = fields.Char(
        string='Purchase Request',
        # related='purchase_id.purchase_number',
        readonly=True,
        # oldname = 'purchase_number'
    )
    product = fields.Char(
        readonly=True,
        # related='purchase_id.product',
        string='ผลผลิต',
        # oldname='purchase_id,product'
    )
    expenses = fields.Char(
        # related='purchase_id.expenses',
        readonly=True,
        string='รายจ่าย',
        # oldname='expenses'
    )
    activity = fields.Char(
        # related='purchase_id.activity',
        readonly=True,
        string='กิจกรรม',
        # oldname='activity'
    )
    detail = fields.Char(
        # related='purchase_id.detail',
        string='รายละเอียด',
        # oldname='detail'
    )
    people_purchase = fields.One2many(
        'res.partner',
        'name',
        # related='purchase_id.people_purchase',
        string='คณะกรรมการจัดซื้อ / จัดจ้าง',
        # oldname='purchase_id,people_purchase'
    )
    people_check_id = fields.One2many(
        'res.partner',
        'name',
        string='คณะกรรมการตรวจรับพัสดุ / การจ้าง',
        # related='purchase_id.people_check_id',
        # oldname='purchase_id,people_check_id'
    )
    faculty_ids = fields.Many2one(
        'faculty.branch',
        # oldname='faculty_ids',
        # related='purchase_id.faculty_ids',
        string='คณะ / สำนักงาน / ศูนย์'
    )
    branch_id = fields.Many2one(
        'bru.faculty',
        # related='purchase_id.branch_id',
        string='สาขา',

    )

