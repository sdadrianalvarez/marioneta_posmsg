se tiene el repositorio https://github.com/sdadrianalvarez/marioneta_posmsg

tengo instancias de odoo en http://caballeroantonio.ddns.net

odoo13e		puerto=8266		db=o13e_pdv2	replica de alfa.contabilidad_pdv
odoo14ce	puerto=8269	db=o14ce_3		pruebas


/pos/message/						pinta un mensaje predefinido por toño, no le estoy sacando provecho, es sólo ejemplificativo, ej: http://caballeroantonio.ddns.net:8266/pos/message
/pos/messages/objects/				pinta la lista de cajas, ej:			http://caballeroantonio.ddns.net:8266/pos/messages/objects
/pos/messages/objects/<int:id>		pinta el detalle de la caja id, ej:		http://caballeroantonio.ddns.net:8266/pos/messages/objects/1
/pos/messages/update/1/un mensaje	guarda un mensaje asociado a la caja, ej:		http://caballeroantonio.ddns.net:8266/pos/messages/update/1/un%20mensaje

#observaciones
- cuando una caja está abierta odoo no la puede editar así que aplico los cambios mediante query

#cookies
- si odoo maneja varias db y hay una cookie que le diga a odoo a qué db debe redireccionar la petición marcará un error, se puede solventar de la siguiente manera:
	- que el primer request sea para elegir la db, ej: http://caballeroantonio.ddns.net:8266/web?db=o13e_pdv2
	- que el segundo request sea para mandar la petición deseada, ej: http://caballeroantonio.ddns.net:8266/pos/message

- si utilizas marionetas selenium puede resultar incómodo cambiar de interfaz para mandar la petición y luego regresar a la interfaz que se tenía, también puede ser incómodo abrir una pestaña adicional porque implica agregar windows-controller adicionales, una forma de solventarlo es enviar el request usando javascript:

```
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.open("GET", "/pos/message");

xhr.send();
```