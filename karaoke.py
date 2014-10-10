#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Alba Oterino Corral

import smallsmilhandler
import sys
import os

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

def imprimir():
    for elementoXML in karaoke.etiquetas:
  
        print elementoXML['etiqueta'], 
               
        clave = elementoXML.keys()
        valor = elementoXML.values()

        for i in range(len(clave)): 
            #si la clave es 'etiqueta' no se saca por pantalla
            #y si el valor del atributo es vacio tampoco se saca por pantalla
            #por tanto solo se saca por pantalla si la clave no es 'etiqueta' y existe un valor
            if clave[i] != "etiqueta" and valor[i] != "":
                print "\t" + clave[i]+"=\""+valor[i]+"\"",
        print "" #print sin , provoca el salto de linea.

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
        #recurso = sys.argv[1]
    except (IndexError):
        print "Usage: python karaoke.py file.smil"
        sys.exit()
    
    #os.system("wget -q" + recurso)
    parser = make_parser() #creo el parse
    karaoke = SmallSMILHandler() #creo objeto
    parser.setContentHandler(karaoke)
    parser.parse(open('karaoke.smil')) #parsea karaoke.smil 
    print karaoke.get_tags()
    imprimir()
    
