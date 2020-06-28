# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Workshop(models.Model):
	_name = "pr.courses.workshops"

	name = fields.Char("Nombre")
	description = fields.Text("Descripción del Taller")
	course_taller_id = fields.Many2one("pr.courses.information", "Curso")
	taller_id = fields.Many2one("pr.diploma.registration", "Diplomado")
	pr_course_section_id = fields.Many2one("pr.course.section", "pr_course_section_id")

	





	
