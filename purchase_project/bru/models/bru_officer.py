# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BruOfficer(models.Model):
    _name = 'bru.officer'
    _rec_name = 'name_sur'
    _description = 'BRU Officer'

    number_id = fields.Char(
        string=u'เลขประจำตัว'
    )
    name_sur = fields.Char(
        string=u'ชื่อ - นามสกุล'
    )
    phone = fields.Char(
        string=u'เบอร์โทรศัพท์'
    )
    faculty_ids = fields.Many2one(
       'bru.faculty',
        string=u'คณะ'
    )
    faculty_branch = fields.Many2one(
        'faculty.branch',
        string=u'สาขา'
    )
    affiliation_id = fields.Char(
        string=u'รหัสหน่วยงานสังกัด'
    )
    affiliation = fields.Char(
        string=u'หน่วยงานสังกัด'
    )
    organization_id = fields.Char(
        string=u'รหัสหน่วยงานปฏิบัติ'
    )
    organization = fields.Char(
        string=u'หน่วยงานปฏิบัติ'
    )
    email = fields.Char(
        string=u'อีเมลล์'
    )
    position = fields.Selection(
        selection=[
            ('m1', u'นาย'),
            ('m2', u'นาง'),
            ('m3', u'นางสาว'),
            ('m4', u'ดร.'),
            ('m5', u'ศาตราจารย์'),
        ],
        string=u'ชื่อตำแหน่ง'
    )
    image = fields.Binary(
        string="Photo")

    # @api.onchange('faculty')
    # def _onchange_faculty(self):
    #     for rec in self:
    #         if rec.faculty:
    #             rec.branch = rec.faculty