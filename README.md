# isitup

[![Latest Version][1]][2]
[![Build Status][3]][4]

> Is it up?

Check whether a website is up or down. Using [isitup][]'s API. Inspired by [is-up][].

## Install

    $ pip install isitup

## Usage

* CLI

        $ isitup github.com
        Yay, github.com is up.
        It took 0.022 ms for a 301 response code with an ip of 192.30.252.130

* API

        >>> from isitup.main import check
        >>> check('github.com')
        u'Yay, github.com is up.\nIt took 0.022 ms for a 301 response code with an ip of 192.30.252.130'

## License

MIT.


[1]: http://img.shields.io/pypi/v/isitup.svg
[2]: https://pypi.python.org/pypi/isitup
[3]: https://travis-ci.org/lord63/isitup.svg
[4]: https://travis-ci.org/lord63/isitup
[isitup]: https://isitup.org/api/api.html
[is-up]: https://github.com/sindresorhus/is-up
