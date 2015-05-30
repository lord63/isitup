#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests


def check(url):
    response = requests.get("http://isitup.org/{0}.json".format(url)).json()
    status_code = response["status_code"]
    if status_code == 1:
        time, code, ip = (response['response_time'], response['response_code'],
                          response['response_ip'])
        return ("Yay, {0} is up.\nIt took {1} ms for a {2} response code "
                "with an ip of {3}".format(url, time, code, ip))
    if status_code == 2:
        return "{0} seems to be down!"
    if status_code == 3:
        return "We need a valid domain to check! Try again."
