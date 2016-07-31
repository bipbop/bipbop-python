import unittest
import xml.etree.ElementTree as ET
from bipbop.client import WebService
from bipbop.client import ServiceDiscovery

class BipbopTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ws = WebService('907703004bbdd0a7f11e0398b5f200ac')
        cls.sd = ServiceDiscovery.factory(cls.ws)

    def test_basicWebservice(self):
        xml = self.ws.post("SELECT FROM 'PLACA'.'CONSULTA'", {'placa': 'OGD1557'})
        self.assertFalse(xml is None)

    def test_listDatabase(self):        
        self.assertTrue(len(list(self.sd.list_databases())) > 0)

    def test_getDbName(self):
        db = self.sd.get_database('CORREIOS')
        self.assertEqual('CORREIOS', db.name())

    def test_getTableName(self):
        db = self.sd.get_database('CORREIOS')
        table = db.get_table('CONSULTA')
        self.assertEqual('CONSULTA', table.name())

    def test_getFieldName(self):
        db = self.sd.get_database('CORREIOS')
        table = db.get_table('CONSULTA')
        self.assertEqual('cep', list(table.get_fields())[0].name())

    def test_traverseDb(self):
        for db in self.sd.list_databases():
            self.assertIsNotNone(db.get('name'))
            odb = self.sd.get_database(db.get('name'))
            self.assertIsNotNone(odb)            
            for table in odb.list_tables():
                self.assertIsNotNone(table.get('name'))
                otb = odb.get_table(table.get('name'))
                self.assertIsNotNone(otb)                
                for field in otb.get_fields():
                    self.assertIsNotNone(field.name())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BipbopTest)
    unittest.TextTestRunner(verbosity=2).run(suite)