#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import urllib.request
from urllib.error import HTTPError, URLError

def main(url, archivo):
    # momento actual
    ahora = time.time()

    try:
        descarga = urllib.request.urlopen(url)
        print("Descargando... ", url)
        # modo b de binario w de escritura
        fichero = open(archivo, "wb")
        fichero.write(descarga.read())
        fichero.close()
        tiempo_transcurrido = time.time() - ahora
        print("Archivo guardado: %s en %0.3fs" % (archivo, tiempo_transcurrido))


    except HTTPError as e:
        print("Error HTTP: ", e.code, url)


    except URLError as e:
        print("Error URL: ", e.reason, url)


if __name__ == "__main__":

    if (sys.argv[1] == '--help') or (sys.argv[1] == '-h'):
        print('- Uso: python3 descarga.py url nombre')
        sys.exit()
    if (sys.argv[1] == '--version') or (sys.argv[1] == '-v'):
        print('- Compatible con python 3 o superiores.\nwww.tostring.es')
        sys.exit()
    if len(sys.argv) != 3:
        print('- Sólo se aceptan dos argumentos.')
        sys.exit()

    url = sys.argv[1]
    archivo = sys.argv[2]
    main(url, archivo)

