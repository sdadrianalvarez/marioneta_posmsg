se tiene el repositorio https://github.com/sdadrianalvarez/marioneta_posmsg

tengo instancias de odoo en http://caballeroantonio.ddns.net

odoo13e		db=o13e_pdv2	replica de alfa.contabilidad_pdv
odoo14ce	db=o14ce_3		pruebas


/pos/message/						pinta un mensaje predefinido por toño, no le estoy sacando provecho, es sólo ejemplificativo, ej: http://caballeroantonio.ddns.net:8266/pos/message
/pos/messages/objects/				pinta la lista de cajas, ej:			http://caballeroantonio.ddns.net:8266/pos/messages/objects
/pos/messages/objects/<int:id>		pinta el detalle de la caja id, ej:		http://caballeroantonio.ddns.net:8266/pos/messages/objects/1
/pos/messages/update/1/un mensaje	guarda un mensaje asociado a la caja, ej:		http://caballeroantonio.ddns.net:8266/pos/messages/update/1/un%20mensaje

#observaciones
- cuando una caja está abierta odoo no la puede editar así que aplico los cambios mediante query
- 