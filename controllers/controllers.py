# -*- coding: utf-8 -*-
from odoo import http

class MarionetaPosmsgController(http.Controller):
	@http.route('/pos/message/', auth='public')
	def index(self, **kw):
		return 'Hello, world'

	@http.route('/pos/messages/objects/', auth='public')
	def list(self, **kw):
		return http.request.render('marioneta_posmsg.listing', {
			'root': '/pos/messages',
			'objects': http.request.env['pos.config'].search([]),
		})

	@http.route('/pos/messages/objects/<model("pos.config"):obj>/', auth='public')
	def object(self, obj, **kw):
		return http.request.render('marioneta_posmsg.object', {
			'object': obj
		})

	@http.route('/pos/messages/update/<int:id>/<string:message>/', auth='public')
	def update(self, **kw):
		
		cashier = http.request.env['pos.config'].search([('id','=',  kw['id'] )])
		if cashier:
			#odoo.exceptions.UserError: ('No se puede modificar esta configuración de PdV porque hay una sesión de PdV abierta basada en ella.', '') 
			#cashier['message'] = kw['message']
			
			
			query = "UPDATE pos_config SET message = %s WHERE id = %s"
			http.request.env.cr.execute(query, (kw['message'], kw['id']) )
			# return http.request.render('marioneta_posmsg.object', {
				# 'object': cashier
			# })
			return '1'
		else:
			return '0'
		
