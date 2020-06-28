# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_MiniCamp(models.Model):
	_name = "pr.course.minicamp"


	name = fields.Char("Nombre")
	description = fields.Text("Descripción del Mini Campamento")
	courseminicamp_id = fields.Many2one("pr.courses.information", "Curso")
	minicam_id = fields.Many2one("pr.course.section", "Seccion")
	initial_date= fields.Date("Fecha de Inicio")
	final_date = fields.Date("Fecha Final")



	