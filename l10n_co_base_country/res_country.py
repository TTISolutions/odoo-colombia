# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class ResCountry(models.Model):
    _inherit = 'res.country'

    code_dian = fields.Char(
        string=u'Código Dian',
        required=False,
        readonly=True)
