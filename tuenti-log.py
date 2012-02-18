#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-dd

# Autor: Alberto Alcolea
# Date:  18-2-2012

# IMPORTAN!! This script run correctly in Python 2.7


import sys
import re
import pycurl

# Constantes
URL_BASE = 'http://ak3.img.tuenti.net/'
#~~~~~~~~~~~~~~~~~~

# Crea el objeto cURL y llama a sus meodos para descargar una URL
# en el fichero indicado. Devuelve el codigo de estado HTTP devuelto
# por la URL.
def curl_downfile(url, filename):
  c = pycurl.Curl()
  c.setopt(c.URL, url)
  c.setopt(c.USERAGENT, 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8');
  c.setopt(c.WRITEDATA, file(filename, 'wb'))
  c.setopt(c.NOPROGRESS, 0)
  print ' Downloading ' + filename
  try:
    s = c.perform()
  except error, e:
    if code in (7,52):
      print >> sys.stderr, 'ERRORRRRRRRRR!!!!'
  print ' Downloading finished.'
  status = c.getinfo(c.HTTP_CODE)
  c.close()
  return status


# Abre un fichero de texto con un log de paquetes TCP/IP y devuelve una
# lista con los que corresponden con regExp.
def read_file(filename, regExp):
  f = open(filename, 'r')
  raw = f.read()
  f.close()
  return re.findall(regExp, raw)


def buscar_en_lista(list, x):
  for i in list:
    if i == x: return i[1]
  return -1


# main()
def main():
  if len(sys.argv) < 2:
    print '  Debes introducir un fichero con los logs de paquetes capturados.'
    sys.exit(-1)

  tuples = read_file(sys.argv[1], r'HTTP 4\d\d GET /([\w\-_]+)')

  imagenes = []
  
  if len(tuples) > 0:  
  
    # Quitamos repetidos
    for tuple in tuples:
      if buscar_en_lista(imagenes, tuple) == -1:
        imagenes.append(tuple)
    
    # Descargamos
    for tuple in imagenes:
      curl_downfile(URL_BASE + tuple, tuple + '.jpg')

if __name__ == '__main__':
  main()
