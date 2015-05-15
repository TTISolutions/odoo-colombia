# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.one
    @api.depends('name', 'first_name', 'middle_name', 'last_name', 'second_last_name')
    def copy(self, default=None):
        default = default or {}
        if self.is_company:
            default.update({
                'name': self.name and self.name + '(copy)' or '',
            })
        else:
            default.update({
                'first_name': self.first_name and self.first_name + '(copy)' or '',
                'middle_name': self.middle_name and self.middle_name + '(copy)' or '',
                'last_name': self.last_name and self.last_name + '(copy)' or '',
                'second_last_name': self.second_last_name and self.second_last_name + '(copy)' or '',
            })
        return super(ResPartner, self).copy(default=default)
    
    @api.onchange('first_name', 'middle_name', 'last_name', 'second_last_name')
    def _onchange_name(self):
        names = [name for name in [self.first_name, self.middle_name, self.last_name, self.second_last_name] if name]
        self.name = ' '.join(names)
        
    first_name = fields.Char("First Name")
    middle_name = fields.Char("Second Name")
    last_name = fields.Char("Last Name")
    second_last_name = fields.Char("Second Last Name")
    
    @api.one
    def write(self, vals):
        if not self.is_company:
            names = [name for name in [vals.get('first_name', False) or self.first_name,
                                       vals.get('middle_name', False) or self.middle_name, 
                                       vals.get('last_name', False) or self.last_name, 
                                       vals.get('second_last_name', False) or self.second_last_name] if name]
            vals.update({
                'name': ' '.join(names),
            })
        return super(ResPartner, self).write(vals)
