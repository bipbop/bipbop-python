# BIPBOP
# -*- coding: utf-8 -*-

import bipbop

class Database:

    KEY_TABLE_NAME = "name"
    KEY_TABLE_DESCRIPTION = "description"
    KEY_TABLE_URL = "url"

    def __init__(self, ws, domNode, dom):
        self.ws = ws
        self.domNode = domNode
        self.dom = dom

    def name(self):
        return self.domNode.get('name')

    def list_tables(self):
        tables = self.domNode.findall('./table')

        for table in tables:
            yield {
                Database.KEY_TABLE_NAME: table.get('name'),
                Database.KEY_TABLE_DESCRIPTION: table.get('description'),
                Database.KEY_TABLE_URL: table.get('url')
            }

    def get_table(self, name):
        table = self.domNode.find("./table[@name='%s']" % name.strip())

        if table is None:
            raise bipbop.client.Exception("Can't find the table.")
        
        return bipbop.client.Table(self.ws, self, table, self.dom)

    def get(self, attr):
        return self.domNode.get(attr)