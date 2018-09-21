#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/22/18 12:06 AM

import base64
import re
from pprint import pprint


class Ss(object):
    def __init__(self):
        self.plus = '+'
        self.minus = '-'
        self.backslash = r'//'
        self.equal = '='

    def main(self, ssr):
        ssr = re.split(self.backslash, ssr)[-1]

        ssr_decode = self.decode64(ssr)

        ssr_link = re.split(':', ssr_decode)

        params = re.split('/\?', ssr_link[5])

        password = self.decode64(params[0])
        ssr_config = {
            'server': ssr_link[0],
            'server_port': ssr_link[1],
            'protocol': ssr_link[2],
            'method': ssr_link[3],
            'obfs': ssr_link[4],
            'password': password
        }
        if len(params) > 1:
            ssr_config = dict(ssr_config, **self.decode_param(params[1]))
        return ssr_config

    def decode_param(self, params_encoded):
        params_encoded = re.split('&', params_encoded)
        params = {}

        for param in params_encoded:
            param = re.split('=', param)
            params = dict(params, **{param[0]: self.decode64(param[-1])})
        return params

    def decode64(self, string):
        string = self.fit64(string)
        return base64.b64decode(re.sub(self.minus, self.plus, string)).decode('utf-8')

    def encode64(self, string):
        string = self.fit64(string)
        return base64.b64encode(re.sub(self.plus, self.minus, string))

    def fit64(self, string):
        length = len(string)
        missing_padding = 4 - length % 4 if length % 4 else 4
        if missing_padding:
            string += self.equal * missing_padding
        return string


if __name__ == '__main__':
    ssr_url = 'ssr://NjQuMTM3LjIwMS4yNDY6Mjk4NzphdXRoX3NoYTFfdjQ6Y2hhY2hhMjA6dGxzMS4yX3RpY2tldF9hdXRoOlpHOTFZaTVwYnk5emMzcG9abmd2S21SdmRXSXVZbWxrTDNOemVtaG1lQzhxTWprNE53Lz9yZW1hcmtzPTVweXM2TFNtNVktMzVwMmw2SWVxT21SdmRXSXVhVzh2YzNONmFHWjRMLW1Wbk9XRGotV2ZuLVdRalRwa2IzVmlMbUpwWkM5emMzcG9abmd2'
    ss = Ss()
    form = ss.main(ssr_url)
    pprint(form)
