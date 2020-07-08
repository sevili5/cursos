# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning
import time

class WizardAgregarMedicamento(models.TransientModel):
	_name = "clinica.diadema.agregar.medicamento.wizard"

	sicklnes_id = fields.Many2one("clinica.sicklnes", "Enfermedad")
	wizard_agregar_detail_ids = fields.One2many("clinica.diadema.agregar.medicamento.detail.wizard",
	 "wizard_agregar_id", "Detalle Medicamento")


    # wizard de medicamentos
	@api.one
	def agregar_medicamento(self):
		obj_agregar = self.env["doff.diadema.detail.consulta.sicks"]
		id_resp = self.env["doff.diadema.consulta"].search([],order="id desc", limit=1)

		print("botom")
		print(self.wizard_agregar_detail_ids)

		for agregar in self.wizard_agregar_detail_ids:
		    # campos del primer tree a mostrar campos de la ventana emergente todos en archivos .py llenar el json
				add = {
					'sicklnes_id':self.sicklnes_id.id,
					'medicine_id':agregar.medicine_agregar_id.id,
					'medical_presentation':agregar.medical_presentation_agregar_id.id,
					'cantidad':agregar.cantidad_agregar,
					'doff_diadema_consulta_id':id_resp.id
					
				}
				obj_agregar.create(add)


class WizardAgregarMedicamentoDetail(models.TransientModel):
	_name = "clinica.diadema.agregar.medicamento.detail.wizard"

	medicine_agregar_id = fields.Many2one("clinica.medicine","Medicamento")
	medical_presentation_agregar_id = fields.Many2one("clinica.medical.presentation","Presentacion Medicamento")
	cantidad_agregar = fields.Integer("Cantidad")
	wizard_agregar_id = fields.Many2one("clinica.diadema.agregar.medicamento.wizard","Agregar Medicamento")
    




	
		
