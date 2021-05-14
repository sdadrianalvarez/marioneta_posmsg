# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class PosConfig(models.Model):
	

	_inherit = 'pos.config'

	_description = 'Point of Sale Configuration'
	
	
	message = fields.Char(
		
		
		
			
		string='Message'
	
	)
		
	
	
	
	
	
	
