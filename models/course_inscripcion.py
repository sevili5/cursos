# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Registration(models.Model):
	_name = "pr.courses.registration"
	_rec_name = "pr_courses_information_id"
	

	state = fields.Selection([('borrador', 'Borrador'), ('canceled', 'Cancelado'), ('done', 'Finalizado')], string="Estado", default="borrador")
	date= fields.Date("Fecha de Inscripción")
	active = fields.Boolean("Activo", default=True)
	inscripcion = fields.Selection([('curso', 'Curso'), ('taller', 'Taller'), ('otros', 'Otros Eventos')], string="Inscripcion")
	#Many2one
	pr_courses_information = fields.Many2one("pr.courses.information", "Eventos")
	pr_courses_workshops = fields.Many2one("pr.courses.workshops", "Taller")
	ins_id = fields.Many2one("res.users", "Instructor")
	pr_courses_information_id = fields.Many2one("pr.courses.information", "Curso")
	course_section_id = fields.Many2one("pr.course.section", "Seccion")
	#Many2many
	member_ids = fields.Many2many("res.partner", "tabla_relacion_inscripcion_miembro", "inscripcion_id", "miembro_id", "Miembros")

	
	
	@api.onchange("course_section_id")
	def onchange_section(self):
		if self.course_section_id:
			for course in self.course_section_id.curso_taller_ids:
				self.pr_courses_information = course.course_information_id.id
				self.ins_id = course.instructor_id.id


	@api.multi
	def set_state_done(self):
		if self.member_ids:
			self.write({'state': 'done'})


	@api.multi
	def set_state_draft(self):
		self.write({'state': 'borrador'})


	@api.multi
	def set_state_canceled(self):
		self.write({'state': 'canceled'})