# BIPBOP
# -*- coding: utf-8 -*-

class Push:
    PARAMETER_PUSH_QUERY = "pushQuery"
    PARAMETER_PUSH_INTERVAL = "pushInterval"
    PARAMETER_JURISTEK_CALLBACK = "juristekCallback"
    PARAMETER_PUSH_LABEL = "pushLabel"
    PARAMETER_PUSH_AT = "pushAt" # timestamp
    PARAMETER_PUSH_TRY_IN = "pushTryIn"
    PARAMETER_PUSH_MAX_VERSION = "pushMaxVersion"
    PARAMETER_PUSH_EXPIRE = "pushExpire"
    PARAMETER_PUSH_PRIORITY = "pushPriority"
    PARAMETER_PUSH_ID = "id"
    PARAMETER_PUSH_CALLBACK = "pushCallback"

    def __init__(self, webservice):
        self.ws = webservice

    def create(self, label, push_callback, query, parameters):
        params = {}
        params.update(parameters)
        params.update({
                Push.PARAMETER_PUSH_LABEL: label,
                Push.PARAMETER_PUSH_QUERY: query,
                Push.PARAMETER_PUSH_CALLBACK: push_callback
            })
        return self.ws.post("INSERT INTO 'PUSH'.'JOB'", params).find("./body/id").text

    def delete(self, id):
        return self.ws.post("DELETE FROM 'PUSH'.'JOB'",
            {
                'id': id
            })

    def open(self, id, label=None):
        return self.ws.post("SELECT FROM 'PUSH'.'DOCUMENT'",
            {
                'id': id,
                'label': label
            })

    def change_interval(self, id, interval):
        return self.ws.post("UPDATE 'PUSH'.'PUSHINTERVAL'",
            {
                Push.PARAMETER_PUSH_ID: id,
                Push.PARAMETER_PUSH_INTERVAL: interval
            })

    def change_max_version(self, id, max_version):
        return self.ws.post("UPDATE 'PUSH'.'PUSHMAXVERSION'",
            {
                Push.PARAMETER_PUSH_ID: id,
                Push.PARAMETER_PUSH_MAX_VERSION: max_version
            })
