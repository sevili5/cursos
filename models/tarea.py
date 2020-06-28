# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Course_Tarea(models.Model):
    _name = "pr.course.tarea"
    
    name = fields.Char("Nombre")
    description = fields.Text("Descripción de la Tarea")
    