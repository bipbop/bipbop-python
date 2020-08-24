# BIPBOP
# -*- coding: utf-8 -*-

from .push import Push

class PushJuristek(Push):

    PARAMETER_PUSH_JURISTEK_CALLBACK = "juristekCallback"
    PARAMETER_PUSH_JURISTEK_QUERY = "data"

    def create(self, label, push_callback, query, params):
        parameters = {}

        if len(params):
            data = []
            for key, value in params.items():
                data.append("'%s' = '%s'" % (key, value))
            query += ' ' if query.upper().find('WHERE') != -1 else ' WHERE '
            query += ' AND '.join(data)            

        parameters.update(params)
        parameters.update({
            Push.PARAMETER_PUSH_LABEL: label,
            Push.PARAMETER_PUSH_QUERY: "SELECT FROM 'JURISTEK'.'PUSH'",
            PushJuristek.PARAMETER_PUSH_JURISTEK_QUERY: query,
            PushJuristek.PARAMETER_PUSH_JURISTEK_CALLBACK: push_callback
        })

        return self.ws.post("INSERT INTO 'PUSHJURISTEK'.'JOB'", parameters).find("./body/id").text