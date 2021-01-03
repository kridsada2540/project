# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Tambon(models.Model):
    _name = 'tambon'
    _rec_name = 'name'
    _description = 'Tambon'

    name = fields.Char(
        string='Name'
    )
    name_eng = fields.Char(
        string='Name Eng'
    )
    amphur_code = fields.Integer(
        string='Amphur'
    )
    code = fields.Integer()
