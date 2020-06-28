# -*- encoding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta


class Res_Users(models.Model):
    _inherit= "res.users"

    #GENERAL FIELDS 
    es_instructor = fields.Boolean("Es instructor")
  


    

