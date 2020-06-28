# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course_Proyecto(models.Model):
    _name = "pr.course.proyecto"
    
    name = fields.Char("Nombre")
    description = fields.Text("Descripción del Proyecto")

