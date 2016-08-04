# Bipbop Python

Biblioteca em Python para interação com a Bipbop API. Com ela você pode fazer consulta de dados cadastrais, consulta do Perfil Consumidor para SAC, Correios, placas de veículos entre outras bases. Tudo que você precisa é adquirir uma chave de API válida entrando em contato com a Bipbop.

# Buscando o nome através do CPF/CNPJ

Existe uma classe especial chamada `NameByCPFCNPJ` cujo método estático *evaluate* pode ser usado para consultar o nome através do CPF/CNPJ, passando-se o CPF/CNPJ como string e opcionalmente a data de nascimento como DATETIME ou Inteiro:

```python
from bipbop.client import NameByCPFCNPJ
print NameByCPFCNPJ.evaluate(cpf_cnpj, dt_nasc)
```

# Como utilizar

Com uma chave de API válida em mãos você pode interagir com bancos os quais sua chave tem acesso. Nesse repositório você encontrará o arquivo __test.py__ com o codigo a abaixo.

O primeiro passo é saber quais são esses bancos. Para isso temos a classe `ServiceDiscovery` que usa uma instância de `WebService`, criada a partir de sua chave:

```python
from bipbop.client import WebService, ServiceDiscovery

ws = WebService('#SUA API KEY#')
sd = ServiceDiscovery.factory(ws)

print '== Listando todos os databases =='

for dbinfo in sd.list_databases():
    db = sd.get_database(dbinfo.get('name'))
    print 'Database: %s ; Description: %s ; URL: %s' % (db.name(), db.get('description'), db.get('url'))
```

Vamos tomar como exemplo o database __PLACA__ e descobrir quais tabelas podemos consultar e com quais campos:

```python
dbplaca = sd.get_database('PLACA')

print '== Listando tabelas de PLACA =='
for tbinfo in dbplaca.list_tables():
    table = dbplaca.get_table(tbinfo.get('name'))
    print 'Table: %s ; Description: %s ; URL: %s' % (table.name(), table.get('description'), table.get('url'))
```

Nossa listagem retornou a tabela __CONSULTA__ mas quais serão os campos que podemos usar como parâmetros em nossa consulta? Vamos descobrir:

```python
tblconsulta = dbplaca.get_table('CONSULTA')

for field in tblconsulta.get_fields():
    print 'Field: %s' % field.get('name')

```

Nossa busca retornou o campo __placa__.

Com esses dados em mãos torna-se simples montar nossa consulta. Basta utilizarmos o método *post* de `WebService` da seguinte forma:

```python
dom = ws.post("SELECT FROM 'PLACA'.'CONSULTA'", {'placa': 'XXX9999'})
```

Esse método retorna um [ElementTree](https://docs.python.org/2/library/xml.etree.elementtree.html) o qual suporta XPath e escrita do XML para arquivo.

```python
import xml.etree.ElementTree as ET

# Visualizando o XML retornado
print ET.tostring(dom.getroot())

# Salvando o XML
dom.write('output.xml')

# Recuperando a marca do veículo
print dom.find('./body/marca').text
```

#PUSH

Criando um __PUSH__

A criação de PUSHES permite captura/monitoramento, sobre uma determinada fonte de dados, através de uma consulta segundo o padrão bpql.

```python
from bipbop.client import Push
push = Push(webservice)
id = push.create('suaLabel', 'urlDeCallBack' , "SELECT FROM 'PLACA'.'CONSULTA'", {'placa' => 'XXX0000'})
```

Nesse caso para a sua url de callback, será retornado o documento bpql gerado, e são enviados os seguintes parametros no header do server:

```
HTTP_X_BIPBOP_VERSION
HTTP_X_BIPBOP_DOCUMENT_ID
HTTP_X_BIPBOP_DOCUMENT_LABEL
```

__ABRINDO__ um PUSH

Com este método é possível visualizar o documento bpql capturado. 

```ruby
puts push.open(id)
```

__REMOVENDO__ um PUSH

Com este método é possível remover determinado PUSH da lista de uma apiKey.

```ruby
push.delete(id)
```

# Mais informações

Para mais informações e aquisição de uma chave de api acesse [http://api.bipbop.com.br](http://api.bipbop.com.br).
