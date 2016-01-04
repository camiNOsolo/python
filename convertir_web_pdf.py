import easygui as eg
import os

campos = [' Url de la página:',' Nombre Archivo:']
entrada = []
entrada = eg.multenterbox(msg='Convertir página web en archivo PDF', title='www.toString.es', fields=campos, values=())
final = ''

if entrada != None:
	try:
		for c, e in zip(campos,entrada):
			os.system("wkhtmltopdf -s Letter " + e[0] + " " + e[1])
			final = final + c + ' ' + e + '\n'
				
		eg.msgbox(final, 'multenterbox', ok_button='Salir')
	except:

		eg.exceptionbox("No es posible convertir a PDF", "Error")

