#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Alba Oterino Corral


from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.etiquetas = []
        self.tags = ["root-layout", "region", "img", "audio", "textstream"]
        self.atributos = {
            "root-layout": ["width", "height", "background-color"],
            "region": ["id", "top", "botton", "left", "right"],
            "img": ["src", "region", "begin", "dur"],
            "audio": ["src", "begin", "dur"],
            "textstream": ["src", "region"]
        }

    def startElement(self, name, attrs):

        diccionario = {}
        if name in self.tags:
            diccionario['etiqueta'] = name
            for atributo in self.atributos[name]:
                diccionario[atributo] = attrs.get(atributo, "")
            self.etiquetas.append(diccionario)

    def get_tags(self):
        return self.etiquetas

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print cHandler.get_tags()
