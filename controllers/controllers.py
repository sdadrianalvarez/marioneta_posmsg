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
			#'objects': http.request.env['pos.config'].sudo().search([]),
		})

	@http.route('/pos/messages/objects/<model("pos.config"):obj>/', auth='public')
	def object(self, obj, **kw):
		return http.request.render('marioneta_posmsg.object', {
			'object': obj
		})

	#@http.route('/pos/messages/update/<int:id>/<string:message>/', auth='public')
	@http.route('/pos/messages/update/<model("pos.config"):obj>/<string:message>', auth='public')
	def update(self, obj, message, **kw):
		
		#resuelve el problema de caja abierta, pero no resuelve el problema: 
		#odoo.exceptions.AccessError: ("Sorry, you are not allowed to access documents of type 'Point of Sale Session' (pos.session). This operation is allowed for the groups:\n\t- Point Of Sale/User - (Operation: read, User: 4)", None) - - -
		from odoo.addons.point_of_sale.models.pos_config import PosConfig
		result = super(PosConfig, obj).write({'message': message})
		return str(result)
		
		#odoo.exceptions.UserError: ('No se puede modificar esta configuración de PdV porque hay una sesión de PdV abierta basada en ella.', '') 
		obj['message'] = message
		return '1'
	
		#odoo.exceptions.AccessError: ("Sorry, you are not allowed to access documents of type 'Point of Sale Configuration' (pos.config). This operation is allowed for the groups:\n\t- Point Of Sale/Administrator\n\t- Point Of Sale/User - (Operation: read, User: 4)", None) - - -
		query = "UPDATE pos_config SET message = %s WHERE id = %s"
		http.request.env.cr.execute(query, (message, obj['id']) )
		env.cr.commit()
		return '1'
		