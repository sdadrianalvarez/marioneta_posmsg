# -*- coding: utf-8 -*-
{
	'name':					'POS messages',
	'summary':'''
Coloca mensajes para los puntos de venta
	''',
	'description': '''
Coloca mensajes para los puntos de venta
	''',
	'author':					'caballeroantonio',
	'website':					'http://caballeroantonio.ddns.net',
	
	'category':					'Tests',
	'version':					'1.0',
	
	'depends':					['base','point_of_sale'],
	'external_dependencies': {'python': []},
	
	'data': [
		'security/res.groups.xml',
		'security/ir.model.access.csv',
		'views/views.xml',
		'views/templates.xml',
	],
	
	'demo': [
		
	],
	'auto_install':				False,
	'price': 169,
	'currency':					'USD',
	
	
	'application':				True,
	
	
	'installable':				True,
	'license':					'LGPL-3',
	'maintainer':				'caballeroantonio',
	
	
}
