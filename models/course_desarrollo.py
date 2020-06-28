# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Course_Desarrollo(models.Model):
	_name = "pr.course.section.line"

	initial_date= fields.Date("Fecha de Inicio") 
	final_date = fields.Date("Fecha Final")
	course_section_id = fields.Many2one("pr.course.section", "Seccion")
	course_information_id = fields.Many2one("pr.courses.information", "Curso")
	instructor_course_id = fields.Many2one("res.partner", "Instructores")
	pr_course_section_line_ids = fields.One2many("pr.course.instructor.proyecto", "pr_course_section_line_id", "pr_course_section_line_ids")
	course_section_line_ids = fields.One2many("pr.course.instructor.tarea", "course_section_line_id", "course_section_line_ids")
	state = fields.Selection([('borrador', 'Borrador'), ('progreso', 'progreso'), ('done', 'Finalizado')], string="Estado", default="borrador")
	as_course_section_line_ids = fields.One2many("pr.course.asistencias", "as_course_section_line_id", "as_course_section_line_ids")
	instructor_id= fields.Many2one("res.users", "Instructor")


	@api.onchange("course_section_id")
	def onchange_section(self):
		if self.course_section_id:
			for course in self.course_section_id.curso_taller_ids:
				self.pr_courses_information = course.course_information_id.id
				self.instructor_id = course.instructor_id.id


class Course_Instructor_Proyecto(models.Model):
	 _name = "pr.course.instructor.proyecto"
	 
	 pr_course_section_line_id = fields.Many2one("pr.course.section.line", "Desarrollo Instrucor")
	 pr_course_proyecto_id = fields.Many2one("pr.course.proyecto", "Proyecto")
	 description = fields.Text("Descripción del Proyecto")
	 member_id = fields.Many2one("res.partner", "Miembro")


class Course_Instructor_Tarea(models.Model):
	 _name = "pr.course.instructor.tarea"
	 
	 course_section_line_id = fields.Many2one("pr.course.section.line", "Desarrollo Instrutor")
	 pr_course_tarea = fields.Many2one("pr.course.tarea", "Tareas")
	 description = fields.Text("Descripción del Proyecto")
	 member_id = fields.Many2one("res.partner", "Miembro")


class Course_Asistencias(models.Model):
	 _name = "pr.course.asistencias"
	 
	 as_course_section_line_id = fields.Many2one("pr.course.section.line", "Desarrollo")
	 member_id = fields.Many2one("res.partner", "Miembro")
	 horario = fields.Float("Horario Inicial")
	 horario_fin = fields.Float("Horario Final")
	 initial_date= fields.Date("Fecha de Inicio") 
	 final_date = fields.Date("Fecha Final")
	 asistencia = fields.Boolean(string="Asistencia", default=False)