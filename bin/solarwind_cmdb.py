#!/usr/bin/env python3

# pylint: disable=C0209

"""
Exaplanation: solarwind_cmdb a wrapper to collect information from SolarWindws Orion CMDB

Usage:
   $ python  solarwind_cmdb  [ options ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           solarwind_cmdb
    @version        1.00
    @author-name    Wayne Kirk Schmidt
    @author-email   wayne.kirk.schmidt@changeis.co.jp
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html

Reference:
    https://github.com/solarwinds/orionsdk-python
    https://github.com/solarwinds/orionsdk-python/blob/master/samples/query.py

"""

__version__ = 1.00
__author__ = "Wayne Kirk Schmidt (wayne.kirk.schmidt@changeis.co.jp)"

import sys
import json
import argparse
import orionsdk

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""
autotask_ticket creates a ticket in autotask from the data sent to it in JSON format
""")

PARSER.add_argument("-p", metavar='<password>', dest='my_password', \
                    help="specify password")
PARSER.add_argument("-u", metavar='<username>', dest='my_username', \
                    help="specify username")
PARSER.add_argument("-e", metavar='<endpoint>', dest='my_endpoint', \
                    help="specify endpoint server")

ARGS = PARSER.parse_args()

username = ARGS.my_username
password = ARGS.my_password
endpoint = ARGS.my_endpoint

def main():
    """
    Drive for selection. We will need to put in appropriate SQL.
    """
    swisobject = orionsdk.SwisClient(endpoint, username, password)

    results = swisobject.query("SELECT TOP 3 NodeID, DisplayName FROM Orion.Nodes")

    for row in results['results']:
        print("{NodeID:<5}: {DisplayName}".format(**row))

    jsonresults = json.dumps(results)
    print(jsonresults)

if __name__ == '__main__':
    main()
