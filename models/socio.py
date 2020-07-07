# -*- encoding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta


class Socios(models.Model):
    _inherit= "res.partner"

    #GENERAL FIELDS 
    fecha_cumple = fields.Date("Fecha de nacimiento")
    genero = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string='Género')
    numero_identidad = fields.Char("# Identidad")
    es_socio = fields.Boolean("Es socio")
    es_instructor = fields.Boolean("Es instructor")
    es_voluntario = fields.Boolean("Es voluntario")
    es_miembro = fields.Boolean("Es Miembro")
    es_miembro = fields.Boolean("Es Miembro")
    es_aspirante = fields.Boolean("Es Aspirante Instructor")
    es_interesado = fields.Boolean("Asptantes Inscripción")
    edad = fields.Integer("Edad")
    pr_cursos_miembros = fields.Many2one("pr.cursos.miembros", "Curso Miembros")
    inscripcion_ids = fields.Many2many("pr.courses.registration", "tabla_relacion_inscripcion_miembro", "miembro_id", "inscripcion_id", string='Miembros')
    codigo = fields.Integer("Codigo")

    @api.depends("fecha_cumple")
    def calcular_edad(self):
        for x in self:
            if self.fecha_cumple:
                fecha_hoy = str(fields.Date.today())
                hoy = (datetime.strptime(fecha_hoy, '%Y-%m-%d'))
                edad = hoy.year - datetime.strptime(self.fecha_cumple, '%Y-%m-%d').year
                self.edad = edad

