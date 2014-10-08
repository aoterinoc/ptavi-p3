#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Alba Oterino Corral

import sys

from xml.sax import make_parser
from xml.sax.handler import ContentHandler





if __name__ == "__main__":
    if(len(sys.argv) < 1):
        print "Usage: python karaoke.py file.smil"
