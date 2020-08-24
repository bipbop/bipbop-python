# BIPBOP
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

class Field:
    def __init__(self, table, db, domNode, dom):
        self.table = table
        self.db = db
        self.domNode = domNode
        self.dom = dom

    def get(self, attr):
        return self.domNode.get(attr)

    def read_options(self, nodeList):
        return [ ( n.get('value'), n.text ) for n in nodeList ]

    def options(self):
        return self.read_options(self.domNode.findall('./option'))
    
    def name(self):
        return self.get('name')

    def group_options(self):
        return [(g.get('value'), self.read_options(g.findall('./option'))) 
                    for g in self.domNode.findall('./optgroup')]