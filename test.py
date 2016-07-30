from bipbop.client import Database
from bipbop.client import NameByCPFCNPJ
from bipbop.client import WebService
from bipbop.client import ServiceDiscovery
from bipbop.client import Push

push = Push(WebService('907703004bbdd0a7f11e0398b5f200ac')).create("TESTE", "http://127.0.0.1/", "SELECT FROM 'RFB'.'CERTIDAO'", {
    "documento" : "37554311816",
    "nascimento" : "08/06/1990",
    Push.PARAMETER_PUSH_MAX_VERSION : 1
});
