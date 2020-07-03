# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Themes(models.Model):
	_name = "pr.course.themes"


	name = fields.Char("Nombre")
	description = fields.Text("Descripción")
	course_themes_id = fields.Many2one("pr.courses.information","Eventos")


	