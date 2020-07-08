# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning
import time


class WizardReportMedicamento(models.TransientModel):
	_name = "clinica.diadema.report.medicamento.wizard"

	wizard_report_detail_ids = fields.One2many("clinica.diadema.report.medicamento.detail.wizard",
	 "wizard_report_id", "Medicamento")



class WizardReportMedicamentoDetail(models.TransientModel):
	_name = "clinica.diadema.report.medicamento.detail.wizard"

	name = fields.Char("Nombre del Medicamento")
	medicine_report_id = fields.Many2one("clinica.medicine","Medicamento")
	medical_presentation_report_id = fields.Many2one("clinica.medical.presentation","Presentacion Medicamento")
	cantidad = fields.Integer("Cantidad")
	code_medicine = fields.Char("Código")
	wizard_report_id = fields.Many2one("clinica.diadema.report.medicamento.wizard","wizard_report_id")
	




	
		
