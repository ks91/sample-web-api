# -*- coding: utf-8 -*-
"""
Copyright (c) 2022 Kenji Saito

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import requests
import sys


HEADERS = {'Content-Type': 'application/json'}
PREFIX_API = 'http://localhost:5000/'


# This program simply adds up 1 through 10.
if __name__ == '__main__':

    dParam = {
        'name': 'sum'
    }

    r = requests.post(PREFIX_API + 'create', headers=HEADERS,
            data=json.dumps(dParam, indent=2))
    if r.status_code != 200:
        print(r)
        sys.exit(0)

    dParam = {
        'value': '0'
    }

    r = requests.post(PREFIX_API + 'push/sum', headers=HEADERS,
            data=json.dumps(dParam, indent=2))
    if r.status_code != 200:
        print(r)
        sys.exit(0)

    r = requests.get(PREFIX_API + 'peek/sum')
    if r.status_code != 200:
        print(r)
        sys.exit(0)

    print(json.dumps(r.json(), indent=2))

    for i in range(1, 11):
        dParam = {
            'value': [str(i), 'ADD']
        }

        r = requests.post(PREFIX_API + 'push/sum', headers=HEADERS,
                data=json.dumps(dParam, indent=2))
        if r.status_code != 200:
            print(r)
            sys.exit(0)

        r = requests.post(PREFIX_API + 'run/sum')
        if r.status_code != 200:
            print(r)
            sys.exit(0)

        r = requests.get(PREFIX_API + 'peek/sum')
        if r.status_code != 200:
            print(r)
            sys.exit(0)

        print(json.dumps(r.json(), indent=2))


# end of sum.py
