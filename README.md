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

ws = WebService('907703004bbdd0a7f11e0398b5f200ac')
sd = ServiceDiscovery.factory(ws)

print '== Listando todos os databases =='

for dbinfo in sd.list_databases():
    db = sd.get_database(dbinfo.get('name'))
    print 'Database: %s ; Description: %s ; URL: %s' % (db.name(), db.get('description'), db.get('url'))
```

Vamos tomar como exemplo o database __PLACA__ e descobrir quais tabelas podemos consultar e com quais campos:

```php
$databasePlaca = $serviceDiscovery->getDatabase("PLACA");
printf("\n== Listando tabelas de PLACA ==\n\n");
foreach ($databasePlaca->listTables() as $tableInformation) {
    /* @var $database \BIPBOP\Client\Database */
    $table = $databasePlaca->getTable($tableInformation["name"]);
    printf("Available Table: %s\nDescription: %s\nURL: %s\n\n", $table->name(), $table->get("description"), $table->get("url"));
}
```

Nossa listagem retornou a tabela __CONSULTA__ mas quais serão os campos que podemos usar como parâmetros em nossa consulta? Vamos descobrir:

```php
$tableConsulta = $databasePlaca->getTable("CONSULTA");
printf("\n== Listando campos de CONSULTA ==\n\n");
foreach ($tableConsulta->getFields() as $field) {
	printf("Available Field: %s\n\n", $field->name());
}
```

Nossa busca retornou o campo __placa__.

Com esses dados em mãos torna-se simples montar nossa consulta. Basta utilizarmos o método *post* de `WebService` da seguinte forma:

```php
$dom = $webService->post("SELECT FROM 'PLACA'.'CONSULTA'", [
    "placa" => "XXX9999"
]);
```

Esse método retorna um [DOMDocument](http://php.net/manual/en/class.domdocument.php) que pode ser manipulado utilizando a [DOMXPath](http://php.net/manual/en/class.domxpath.php) ambas as classes nativas do PHP.

```php
// Visualizando as tags do documento retornado
printf($dom->saveXML());

// Recuperando a marca do veículo
$xpath = new \DOMXpath($dom);
printf($xpath->evaluate("string(/BPQL/body/marca/.)"));
```

# Mais informações

Para mais informações e aquisição de uma chave de api acesse [http://api.bipbop.com.br](http://api.bipbop.com.br).
