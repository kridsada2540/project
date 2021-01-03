# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Province(models.Model):
    _name = 'province'
    _rec_name = 'name'
    _description = 'Province'

    name = fields.Char(
        string='Name'
    )
    name_eng = fields.Char(
        string='Name Eng'
    )
    code = fields.Integer()
