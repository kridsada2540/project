# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Amphur(models.Model):
    _name = 'amphur'
    _rec_name = 'name'
    _description = 'Amphur'

    name = fields.Char(
        string='Name'
    )
    name_eng = fields.Char(
        string='Name Eng'
    )
    province_id = fields.Many2one(
        'province',
        stirng='Province'
    )
    code = fields.Integer()
