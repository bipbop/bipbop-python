# BIPBOPB
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

class Receiver:

    def __init__(self, headers):
        self.version = headers.get("Http_x_bipbop_version")
        self.docId = headers.get("Http_x_bipbop_document_id")
        self.label = headers.get("Http_x_bipbop_document_label")

    def document(self, content):
        dom = ET.fromstring(content)
        return ET.ElementTree(dom)