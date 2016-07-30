from bipbop.client import Database
from bipbop.client import NameByCPFCNPJ
from bipbop.client import WebService
from bipbop.client import ServiceDiscovery

import xml.etree.ElementTree as ET

ws = WebService('907703004bbdd0a7f11e0398b5f200ac')

"""
xml = ws.post("SELECT FROM 'PLACA'.'CONSULTA'", {'placa': 'OGD1557'})
if not xml is None:
    print ET.tostring(xml.getroot())
    xml.write('output.xml')
"""

sd = ServiceDiscovery.factory(ws)

"""
for db in sd.list_databases():
    odb = sd.get_database(db.get('name'))
    print 'DB: ' + odb.name() + ' - ' + odb.get('description')
    for table in odb.list_tables():
        otb = odb.get_table(table.get('name'))
        print '- Table: ' + table.get('name')
        for field in otb.get_fields():
            print '\t- Field: ' + field.name() 
            #print field.options()
            print field.group_options()

    print 
"""

db = sd.get_database('CORREIOS')

print db.name()
for table in db.list_tables():
    print table

table = db.get_table('CONSULTA')

print table.name()

for fields in table.get_fields():
    print fields.name()
    print fields.options()

