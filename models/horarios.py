# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Horarios(models.Model):
	_name = "pr.course.horarios"
	
	name = fields.Char("Nombre")
	n_dias = fields.Integer("Numero")


