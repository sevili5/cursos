# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class Course_Section(models.Model):
	_name = "pr.course.section"


	name = fields.Char("Nombre")
	initial_date= fields.Date("Fecha Inicial") 
	final_date = fields.Date("Fecha Final")
	curso_taller_ids = fields.One2many("pr.course.section.line", "course_section_id", "Secciòn")
	diplomado_id = fields.Many2one("pr.diploma.registration", "Diplomado")
	state = fields.Selection([('borrador', 'Borrador'), ('progreso', 'Progreso'), ('done', 'Finalizado')], string="Estado", default="borrador")
	lugar = fields.Char("Lugar que se imparte")
	pr_courses_workshops_ids = fields.One2many("pr.courses.workshops", "pr_course_section_id", "pr_courses_workshops_ids")
	pr_course_taller_line_ids = fields.One2many("pr.course.taller.line", "course_section_id", "pr_course_taller_line_ids")
	active = fields.Boolean("Activo", default=False)
	pr_course_section_ids = fields.One2many("pr.course.horario.line", "pr_course_section_id", "Cursos")
	partner_ids = fields.Many2many("res.partner", string="Miembros")	

	

	
class Course_Section_Line(models.Model):
	_name = "pr.course.section.line"

	initial_date= fields.Date("Fecha de Inicio") 
	final_date = fields.Date("Fecha Final")
	course_section_id = fields.Many2one("pr.course.section", "Seccion")
	course_information_id = fields.Many2one("pr.courses.information", "Curso/Taller")
	instructor_course_id = fields.Many2one("res.partner", "Aspirante")
	instructor_id = fields.Many2one("res.users", "Instructor")

	
	
	
class Course_Taller_Line(models.Model):
	_name = "pr.course.taller.line"
	
	
	course_section_id = fields.Many2one("pr.course.section", "Seccion")
	pr_courses_workshops_id = fields.Many2one("pr.courses.workshops", "Taller")
	initial_date= fields.Date("Fecha de Inicio") 
	final_date = fields.Date("Fecha Final")
	instructo_course_id = fields.Many2one("res.partner", "Instructor")
	instructor_id = fields.Many2one("res.users", "Instructor")
	

class Course_Horario_Line(models.Model):
	_name = "pr.course.horario.line"
	
	pr_course_section_id = fields.Many2one("pr.course.section", "Seccion")
	pr_course_horarios_id = fields.Many2one("pr.course.horarios", "Dia")
	horario = fields.Float("Horario Inicial")
	horario_fin = fields.Float("Horario Final")



	