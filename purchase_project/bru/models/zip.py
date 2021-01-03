# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Zip(models.Model):
    _name = 'zip'
    _rec_name = 'name'
    _description = 'Zip'

    name = fields.Char(
        string='Zip'
    )
    tambon_code = fields.Integer(
        string='Tambon'
    )
    province_code = fields.Integer(
        string='Province'
    )
    amphur_code = fields.Integer(
        string='Amphur'
    )
    code = fields.Integer()
