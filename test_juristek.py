from bipbop.client import WebService


def query_arguments(query, params):
    data = []
    for key, value in params.items():
        data.append("'%s' = '%s'" % (key, value))
    query += ' ' if query.upper().find('WHERE') != -1 else ' WHERE '
    query += ' AND '.join(data)
    return query


ws = WebService()
response = ws.post("SELECT FROM 'JURISTEK'.'DATALAKE'", {
    "data": query_arguments("SELECT FROM 'DATALAKE'.'NOME'", {
        'nome': 'HOSPITAL SANTA JOANA',
        'inicio': '2019/08/10',
        'fim': '2020/08/10',
        'filter': 'andamento',
        'limit': 100,
        'skip': 1
    })
})


def get_text(item, query):
    field = item.find(query)
    if field is None:
        return None
    return field.text


for item in response.findall('./body/advogado/processos/processo'):
    print({
        "nome_parte": get_text(item, './nome_parte'),
        "tribunal_nome": get_text(item, './tribunal_nome'),
        "tribunal_consulta": get_text(item, './tribunal_consulta'),
        "parte": get_text(item, './parte'),
        "polo": get_text(item, './polo'),
        "numero_processo": get_text(item, './numero_processo'),
        "primeiro_andamento": get_text(item, './primeiro_andamento'),
    })
