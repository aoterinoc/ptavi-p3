#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Alba Oterino Corral

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
    
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""        
        self.etiquetas = []
   
    def startElement(self, name, attrs):

     if name == 'root-layout':
        rootlayout = {}
        self.width = attrs.get('width',"")
        rootlayout['width'] = self.width
        self.height = attrs.get('height',"")
        rootlayout['height'] = self.height
        self.backgroundcolor = attrs.get('background-color',"")
        rootlayout['background-color'] = self.backgroundcolor
        print "diccionario rootlayout"
        print rootlayout
        self.etiquetas.append(rootlayout)

     elif name == 'region':
        region = {}
        self.id = attrs.get('id',"")
        region['id'] = self.id       
        self.top = attrs.get('top',"")
        region['top'] = self.top
        self.bottom = attrs.get('bottom',"")
        self.left = attrs.get('left',"")
        region['left'] = self.left
        self.right = attrs.get('right',"")
        region['right'] = self.right
        print "diccionario region"
        print region
        self.etiquetas.append(region)

     elif name == 'img':
        img = {}
        self.src = attrs.get('src',"")
        img['src'] = self.src
        self.region = attrs.get('region',"")
        img['region'] = self.region
        self.begin = attrs.get('begin',"")
        img['begin'] = self.region
        self.dur = attrs.get('dur',"")
        img['dur'] = self.dur
        print "diccionario imagen"
        print img
        self.etiquetas.append(img)    
     elif name == 'audio':
        audio = {}
        self.src = attrs.get('src',"")
        audio['src'] = self.src
        self.begin = attrs.get('begin',"")
        audio['begin'] = self.begin
        self.dur = attrs.get('dur',"")
        audio['dur'] = self.dur     
        print "diccionario audio"
        print audio
        self.etiquetas.append(audio)

     elif name == 'textstream':
        textstream = {}
        self.src = attrs.get('src',"")
        textstream['src'] = self.src
        self.region = attrs.get('region',"")
        textstream['region'] = self.region
        print "diccionario textstream"
        print textstream
        self.etiquetas.append(textstream)

        
    def get_tags(self):
        return self.etiquetas

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler() #objeto
    parser.setContentHandler(cHandler)   
    parser.parse(open('karaoke.smil'))
    print cHandler.get_tags()
    
