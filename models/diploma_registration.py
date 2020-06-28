# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Diploma_Registration(models.Model):
	_name = "pr.diploma.registration"

	name = fields.Char("Nombre")
	description = fields.Text("Descripción del diplomado")
	active = fields.Boolean("Activo", default=True)
	course_information_ids = fields.One2many("pr.courses.information", "diplomado_id", "Cursos")
	taller_ids = fields.One2many("pr.courses.workshops", "taller_id", "Cursos")
	initial_date= fields.Date("Fecha de Inicial del Diplomado")
	final_date = fields.Date("Fecha Final del Diplomado")

	
	
