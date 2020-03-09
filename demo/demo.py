#!env python
# -*- coding: UTF-8 -*-

import requests

data = '{"token":"f87acc3139beeead39f0555587be2745","type":"crawler_search_user","search":"china","num":20}'
response = requests.post('https://service.yundou.me/', data=data)

print(response.text)