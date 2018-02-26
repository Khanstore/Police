# -*- coding: utf-8 -*-

from odoo import models, fields, api


class policeparty(models.Model):
	_inherit='res.partner'
	ispolice=fields.Boolean("is Police")
	idno=fields.Integer('BP/ID no')
	joiningdate=fields.Date('Date Of Joining')
	retiredate=fields.Date('Date of Retirement')
	


class police(models.Model):
    _name = 'police.police'

    name = fields.Char('Police')
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
		
class ribons(models.Model):
	_name='police.ribons'
	name=fields.Char('Ribon' ,required=True)
	starting_date=fields.Date('Starting Date')
	serial=fields.Float('Priority')
	image= fields.Binary('Image', help='Select image here')
	
class force(models.Model):
	_name='police.force'
	_description = 'Force Name' 
	title=fields.Char('Force Title',required=True)
	_sql_constraints = [  
		('title_uniq', 'UNIQUE(title)', 
        'Force title must be unique.') 
		]
