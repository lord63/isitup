#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import click

from isitup.main import check
from isitup import __version__


@click.command(context_settings={'help_option_names': ('-h', '--help')})
@click.argument('url')
@click.version_option(__version__, '-v', '--version', message='%(version)s')
def cli(url):
    """Check whether a website is up or down."""
    click.echo(check(url))
