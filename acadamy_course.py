from openerp import models,fields,api

class acadamy_course(models.Model):
	_name= 'acadamy.course'

	name=fields.Char(string='Name',required='true')
	description=fields.Text()