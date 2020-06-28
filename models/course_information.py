# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Information(models.Model):
	_name = "pr.courses.information"

	name = fields.Char("Nombre")
	description = fields.Text("Descripción")
	active = fields.Boolean("Activo", default=False)
	diplomado_id = fields.Many2one("pr.diploma.registration", "Diplomado")
	practice_log_ids = fields.One2many("pr.courses.information.line", "parent_id", "Práctica")
	N_sesiones = fields.Integer("Numero de Sesiones")
	course_themes_ids = fields.One2many("pr.course.themes", "course_themes_id", "Temas")
	course_minicamp_ids = fields.One2many("pr.course.minicamp", "courseminicamp_id", "MiniCampamento")
	perfil_miembro_id = fields.Many2one("pr.course.perfil.miembro", "PerfilMiembro")
	pr_courses_registration_id = fields.Many2one("pr.courses.registration", "pr_courses_registration_id")
	initial_date= fields.Date("Fecha de Inicio")
	final_date = fields.Date("Fecha Final")
	costo = fields.Float("Costo")
	curso_taller = fields.Selection([('curso', 'Curso'), ('taller', 'Taller')], string="Curso")
	

class Course_Information_Line(models.Model):
	_name = "pr.courses.information.line"


	name = fields.Text("Descripción")
	practice_log_id = fields.Many2one("pr.practice.log", "Práctica")
	parent_id = fields.Many2one("pr.courses.information", "Curso")
	initial_date= fields.Date("Fecha de Inicio")
	final_date = fields.Date("Fecha Final")

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
	perfil_miembro_id = fields.Many2one("pr.course.perfil.miembro", "PerfilMiembro")
	pr_courses_information = fields.Many2one("pr.courses.information", "Curso")

	
	
	




