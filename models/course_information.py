# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Information(models.Model):
	_name = "pr.courses.information"

	name = fields.Char("Nombre")
	description = fields.Text("Descripción")
	active = fields.Boolean("Activo", default=False)
	initial_date= fields.Date("Fecha de Inicio")
	final_date = fields.Date("Fecha Final")
	costo = fields.Float("Costo")
	curso_taller = fields.Selection([('curso', 'Curso'), ('taller', 'Taller'), ('campamentos', 'Campamentos'), ('charlas', 'Charlas'), ('asambleas', 'Asambleas')], string="Tipo de Eventos")
	N_sesiones = fields.Integer("Numero de Sesiones")
	#Many2one
	diplomado_id = fields.Many2one("pr.diploma.registration", "Diplomado")
	perfil_miembro_id = fields.Many2one("pr.course.perfil.miembro", "PerfilMiembro")
	pr_courses_registration_id = fields.Many2one("pr.courses.registration", "pr_courses_registration_id")
	#One2many
	practice_log_ids = fields.One2many("pr.courses.information.line", "parent_id", "Práctica")
	course_themes_ids = fields.One2many("pr.course.themes", "course_themes_id", "Temas")
	course_minicamp_ids = fields.One2many("pr.course.minicamp", "courseminicamp_id", "MiniCampamento")
	
	
	

class Course_Information_Line(models.Model):
	_name = "pr.courses.information.line"


	name = fields.Text("Descripción")
	initial_date= fields.Date("Fecha de Inicio")
	final_date = fields.Date("Fecha Final")
	#Many2one
	practice_log_id = fields.Many2one("pr.practice.log", "Práctica")
	parent_id = fields.Many2one("pr.courses.information", "Curso")

	@api.onchange("practice_log_id")
	def onchange_practica(self):
		if self.practice_log_id:
			self.name = self.practice_log_id.description


class Practice_Log(models.Model):
	_name = "pr.practice.log"

	name = fields.Char("Nombre")
	description = fields.Text("Descripción de Practica Supervisada")
	active = fields.Boolean("Activo", default=True)
	state = fields.Selection([('borrador', 'Borrador'), ('progreso', 'Progreso'), ('done', 'Finalizado')], string="Estado", default="borrador")
	#Many2one
	perfil_miembro_id = fields.Many2one("pr.course.perfil.miembro", "PerfilMiembro")
	pr_courses_information = fields.Many2one("pr.courses.information", "Curso")

	
	
	




