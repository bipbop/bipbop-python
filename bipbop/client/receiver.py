# BIPBOPB
# -*- coding: utf-8 -*-

class Receiver:

    def __init__(self, headers):
        self.version = headers.get("Http_x_bipbop_version")
        self.docId = headers.get("Http_x_bipbop_document_id")
        self.label = headers.get("Http_x_bipbop_document_label")

    def document(self):
        pass