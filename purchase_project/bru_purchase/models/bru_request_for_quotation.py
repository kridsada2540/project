# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError

class RequestForQuotation(models.Model):
    _inherit = 'purchase.order'

    user_id = fields.Many2one(
        'res.users',
        default=lambda self: self.env.user,
    )
    purchase_number = fields.Char(
        string='Purchase Request',
        readonly=True
    )
    document_type = fields.Selection(
        selection=[
            ('PR01', u'PR01=ขออนุมัติซื้อวัสดุ'),
            ('PR02', u'PR02=ขออนุมัติซื้อครุภัณฑ์'),
            ('PR03', u'PR03=ขออนุมัติจัดจ้าง')
        ],
        string=u'ประเภทเอกสาร'
    )
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
        related='budget_id.year_budget_id',
        string=u'ปีงบประมาณ'
    )
    name = fields.Many2one(
        'res.partner',
        string=u'เจ้าหน้าที่พัสดุ'
    )
    branch_id = fields.Many2one(
        'bru.faculty',
        string=u'สาขา'
    )
    faculty_ids = fields.Many2one(
        'faculty.branch',
        string=u'คณะ / สำนักงาน / ศูนย์'
    )
    bru_officer_id = fields.Many2one(
        'bru.branch',
        string=u'ชื่อหน่วยงาน'
    )
    for_use = fields.Char(
        string=u'เพื่อใช้ในงานราชการ'
    )
    budget_id = fields.Many2one(
        'bru.budget',
        string=u'ชื่องบประมาณ'
    )
    product = fields.Char(
        related='budget_id.product',
        readonly=True,
        string=u'ผลผลิต'
    )
    expenses = fields.Char(
        related='budget_id.expenses',
        readonly=True,
        string=u'รายจ่าย'
    )
    activity = fields.Char(
        related='budget_id.activity',
        readonly=True,
        string=u'กิจกรรม'
    )
    detail = fields.Char(
        string=u'รายละเอียด'
    )
    remain_budg_id = fields.Integer(
        readonly=True,
        related='budget_id.remain_budg_id',
        string=u'ยอดงบประมาณคงเหลือ'
    )
    people_purchase = fields.One2many(
        'res.partner',
        'name',
        string=u'คณะกรรมการจัดซื้อ / จัดจ้าง'
    )
    people_check_id = fields.One2many(
        'res.partner',
        'name',
        string=u'คณะกรรมการตรวจรับพัสดุ / การจ้าง'
    )

    @api.multi
    def button_confirm(self):
        res = super(RequestForQuotation, self).button_confirm()
        for order in self:
            remain = order.budget_id.remain_budg_id
            if remain == 0:
                cash_balance = order.budget_id.name - order.amount_total
                if cash_balance < 0:
                    raise UserError(_(u'ยอดเกินกำหนดการสั่งซื้อ!!!'))
                order.budget_id.remain_budg_id = cash_balance
                print (cash_balance)
            elif remain > 0:
                cash_balance2 = remain - order.amount_total
                if cash_balance2 < 0:
                    raise UserError(_(u'ยอดเกินกำหนดการสั่งซื้อ!!!'))
                order.budget_id.remain_budg_id = cash_balance2
                print (cash_balance2)
        return res

    @api.model
    def create(self, values):
        request_purchase = super(RequestForQuotation, self).create(values)
        request_purchase.purchase_number = request_purchase.document_type + request_purchase.create_sequence()
        print(request_purchase.document_type)
        return request_purchase



    def create_sequence(self):
        sequence_template = self.env.ref('bru_purchase.sequence_purchase_request_id')
        model = self.env['ir.model'].sudo().search([
            ('name', '=', 'Purchase Order')
        ], limit=1)

        seq = self.env['sequence.purchase'].sudo().search([
            ('name', '=', 'Sequence Purchase Request'),
            ('model_id', '=', model.id),
        ], order='id desc', limit=1)

        if not seq:
            seq_temp = sequence_template.sudo().copy()
            seq_temp.write({
                'code': 'Sequence Purchase Request',
                'name': 'Sequence Purchase Request',
                # 'prefix': 'CN',
            })
            seq = self.env['sequence.purchase'].sudo().create({
                'name': 'Sequence Purchase Request',
                'model_id': model.id,
                'sequence_id': seq_temp.id,
            })
            print (seq.sequence_id.next_by_id)
        return seq.sequence_id.next_by_id()
