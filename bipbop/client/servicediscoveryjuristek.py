# BIPBOP
# -*- coding: utf-8 -*-

from .servicediscovery import ServiceDiscovery

class ServiceDiscoveryJuristek(ServiceDiscovery):

    PARAMETER_OAB = "OAB"

    @staticmethod
    def factory(ws, params=None):
        parameters = {}
        data = None

        if params:
            parameters.update(params)
            if ServiceDiscoveryJuristek.PARAMETER_OAB in params and params.get(ServiceDiscoveryJuristek.PARAMETER_OAB):
                data = "SELECT FROM 'INFO'.'INFO' WHERE 'TIPO_CONSULTA' = 'OAB'"

        if not data:
            data = "SELECT FROM 'INFO'.'INFO'"

        parameters.update({ 'data':  data })
        return ServiceDiscovery(ws, ws.post("SELECT FROM 'JURISTEK'.'INFO'", parameters))

