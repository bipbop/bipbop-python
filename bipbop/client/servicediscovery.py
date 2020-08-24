# BIPBOP
# -*- coding: utf-8 -*-

import bipbop

class ServiceDiscovery:

    KEY_DATABASE_NAME = "name"
    KEY_DATABASE_DESCRIPTION = "description"
    KEY_DATABASE_URL = "url"

    def __init__(self, ws, dbs):
        self.ws = ws
        self.list_dbs = dbs
        
    @staticmethod
    def factory(ws, params=None):
        return ServiceDiscovery(ws, ws.post("SELECT FROM 'INFO'.'INFO'", params or []))

    factory = staticmethod(factory)

    def list_databases(self):
        dbs = self.list_dbs.findall('./body/database')
        for db in dbs:
            yield {
                ServiceDiscovery.KEY_DATABASE_DESCRIPTION: db.get('description'),
                ServiceDiscovery.KEY_DATABASE_NAME: db.get('name'),
                ServiceDiscovery.KEY_DATABASE_URL: db.get('url')
            }

    def get_database(self, name):
        db = self.list_dbs.find("./body/database[@name='%s']" % name.strip())
        if db is None:
            raise bipbop.client.Exception("Can't find that database.")

        return bipbop.client.Database(self.ws, db, self.list_dbs)