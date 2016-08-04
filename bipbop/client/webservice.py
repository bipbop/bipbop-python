# BIPBOP
# -*- coding: utf-8 -*-

from StringIO import StringIO

import httplib
import urllib
import ssl
import xml.etree.ElementTree as ET
import bipbop.client.exception
import gzip

ssl._create_default_https_context = ssl._create_unverified_context

class WebService:

    FREE_APIKEY = "6057b71263c21e4ada266c9d4d4da613";
    ENDPOINT = "irql.bipbop.com.br";
    REFERRER = ""; #https://juridicocorrespondentes.com.br/";
    PARAMETER_QUERY = "q";
    PARAMETER_APIKEY = "apiKey";

    def __init__(self, api_key=None):
        self.api_key = api_key or WebService.FREE_APIKEY

    def post(self, query, params=None):
        conn = httplib.HTTPSConnection(WebService.ENDPOINT)

        data = {}
        data.update(params or {})
        data.update({
            WebService.PARAMETER_QUERY: query,
            WebService.PARAMETER_APIKEY: self.api_key
        })

        conn.request('POST', '', urllib.urlencode(data), {
            'Referer': WebService.REFERRER,
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept-encoding': 'gzip'
        })
        r = conn.getresponse()
        if r.getheader('content-encoding') == 'gzip':
            dom = ET.fromstring(gzip.GzipFile(fileobj=StringIO(r.read())).read())
        else:
            dom = ET.fromstring(r.read())
        self._assert(dom)

        return ET.ElementTree(dom)

    def _assert(self, dom):
        exception = dom.find('./header/exception');

        if not exception is None:
            source = exception.get('source')
            code = exception.get('code')
            id = exception.get('id')
            pushable = (exception.get('pushable') or exception.get('push')) == 'true'
            message = exception.text

            ex = bipbop.client.Exception("[%s:%s/%s] %s %s" % (code, source, id, message, pushable))
            ex.set_attributes(code, source, id, message, pushable)

            raise ex
