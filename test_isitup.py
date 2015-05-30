#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from isitup import check

import pytest


def test_website_is_up():
    assert check('github.com')[:3] == 'Yay'


def test_website_is_down():
    assert "seems to be down!" in check('justfortestisitup.com')


def test_invalid_domain():
    assert check('invalid_domain')[-10:] == "Try again."
