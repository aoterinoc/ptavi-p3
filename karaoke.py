#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Alba Oterino Corral

import smallsmilhandler
import sys
import os

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

Elemen_Source = ['img', 'audio', 'textstream']


class KaraokeLocal (SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        karaoke = SmallSMILHandler()
        parser.setContentHandler(karaoke)
        parser.parse(fichero)
        self.lista = karaoke.get_tags()

    def __str__(self):
        salida = ""
        for elementoXML in self.lista:
            salida += elementoXML['etiqueta']
            clave = elementoXML.keys()
            valor = elementoXML.values()
            for i in range(len(clave)):
                if clave[i] != "etiqueta" and valor[i] != "":
                    salida += "\t" + clave[i]+"=\""+valor[i]+"\""
            salida += "\n"
        return salida

    def do_local(self):

        for etiqueta in self.lista:
            if etiqueta['etiqueta'] in Elemen_Source:
                source = etiqueta["src"]
                if source.find("http://") != -1:
                #si es distinto de -1 lo he encontrado
                    os.system("wget -q " + source)
                    source = source.split("/")[-1]
                    etiqueta["src"] = source

if __name__ == "__main__":

    try:
        fichero = open(sys.argv[1], 'r')
    except (IndexError):
        print "Usage: python karaoke.py file.smil"
        sys.exit()

    obj = KaraokeLocal(fichero)
    print obj
    obj.do_local()
    print obj
