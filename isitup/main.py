#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import requests


def check(url):
    try:
        response = requests.get(
            "https://isitup.org/{0}.json".format(url),
            headers={'User-Agent': 'https://github.com/lord63/isitup'})
    except requests.exceptions.ConnectionError:
        return ("A network problem(e.g. you're offline; refused connection),"
                "can't check the site right now.")
    except requests.exceptions.Timeout:
        return "The request timed out."
    except requests.exceptions.RequestException as error:
        return "Something bad happened:\n{0}".format(error)
    status_code = response.json()["status_code"]
    if status_code == 1:
        return ("Yay, {0} is up.\nIt took {1[response_time]} ms "
                "for a {1[response_code]} response code with "
                "an ip of {1[response_ip]}".format(url, response.json()))
    if status_code == 2:
        return "{0} seems to be down!".format(url)
    if status_code == 3:
        return "We need a valid domain to check! Try again."
