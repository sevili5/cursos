# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Course_Desarrollo(models.Model):
	_name = "pr.course.section.line"
	_rec_name = "course_section_id"


	initial_date= fields.Date("Fecha de Inicio") 
	final_date = fields.Date("Fecha Final")
	state = fields.Selection([('borrador', 'Borrador'), ('canceled', 'Cancelado'), ('done', 'Finalizado')], string="Estado", default="borrador")
	#Many2one
	course_section_id = fields.Many2one("pr.course.section", "Seccion")
	course_information_id = fields.Many2one("pr.courses.information", "Eventos")
	instructor_course_id = fields.Many2one("res.partner", "Instructores")
	instructor_id= fields.Many2one("res.users", "Instructor")
	#One2many
	pr_course_section_line_ids = fields.One2many("pr.course.instructor.proyecto", "pr_course_section_line_id", "pr_course_section_line_ids")
	course_section_line_ids = fields.One2many("pr.course.instructor.tarea", "course_section_line_id", "course_section_line_ids")
	as_course_section_line_ids = fields.One2many("pr.course.asistencias", "as_course_section_line_id", "as_course_section_line_ids")

	@api.onchange("course_section_id")
	def onchange_section(self):
		if self.course_section_id:
			for course in self.course_section_id.curso_taller_ids:
				self.pr_courses_information = course.course_information_id.id
				self.instructor_id = course.instructor_id.id


class Course_Instructor_Proyecto(models.Model):
	 _name = "pr.course.instructor.proyecto"
	 
	 description = fields.Text("Descripción del Proyecto")
	 pr_course_section_line_id = fields.Many2one("pr.course.section.line", "Desarrollo Instrucor")
	 pr_course_proyecto_id = fields.Many2one("pr.course.proyecto", "Proyecto")
	 member_id = fields.Many2one("res.partner", "Miembro")


class Course_Instructor_Tarea(models.Model):
	 _name = "pr.course.instructor.tarea"
	 
	 description = fields.Text("Descripción del Proyecto")
	 course_section_line_id = fields.Many2one("pr.course.section.line", "Desarrollo Instrutor")
	 pr_course_tarea = fields.Many2one("pr.course.tarea", "Tareas")
	 member_id = fields.Many2one("res.partner", "Miembro")


class Course_Asistencias(models.Model):
	 _name = "pr.course.asistencias"
	 
	
	 horario = fields.Float("Horario Inicial")
	 horario_fin = fields.Float("Horario Final")
	 initial_date= fields.Date("Fecha de Inicio") 
	 final_date = fields.Date("Fecha Final")
	 asistencia = fields.Boolean(string="Asistencia", default=False)
	 as_course_section_line_id = fields.Many2one("pr.course.section.line", "Desarrollo")
	 member_id = fields.Many2one("res.partner", "Miembro")