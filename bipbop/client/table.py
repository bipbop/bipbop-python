# BIPBOP
# -*- coding: utf-8 -*-

import bipbop
import push

class Table:

    def __init__(self, ws, db, domNode, dom):
        self.ws = ws
        self.db = db
        self.domNode = domNode
        self.dom = dom
        self.xpath = ""

    def name(self):
        return self.domNode.get('name')

    def get_fields(self):
        fields = self.domNode.findall('./field')
        for field in fields:
            yield bipbop.client.Field(self, self.db, field, self.dom)

    def validate_parameters(self, params):
        pass

    def generate_push(self, parameters, label, push_callback, push_class=push.Push):
        push_obj = push_class(self.ws)
        self.validate_parameters(parameters)
        query = "SELECT FROM '%s'.'%s'" % (self.db.name(), self.name())
        return push_obj.create(label, push_callback, query, parameters)

    def get(self, attr):
        return self.domNode.get(attr)