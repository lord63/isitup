#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from isitup.main import check

import pytest
from click import UsageError
from click import ClickException


def test_website_is_up():
    assert check('github.com')[:3] == 'Yay'


def test_website_is_down():
    with pytest.raises(ClickException) as exception:
        check('justfortestisitup.com')
    assert "seems to be down!" in str(exception.value)


def test_invalid_domain():
    with pytest.raises(UsageError) as exception:
        check('invalid_domain')
    assert "Try again." == str(exception.value)[-10:]
