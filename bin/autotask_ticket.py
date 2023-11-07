#!/usr/bin/env python3

# pylint: disable=C0209

"""
Exaplanation: autotask_ticket a wrapper to create an autotask ticket and get the URL/number

Usage:
   $ python  autotask_ticket  [ options ]

Style:
   Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

    @name           autotask_ticket
    @version        1.00
    @author-name    Wayne Kirk Schmidt
    @author-email   wayne.kirk.schmidt@changeis.co.jp
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html

Sample Data:
    {
        "AccountId": "12345678", 
        "ContactId": "0000001", 
        "DueDateTime": "2021-03-20 00:01:00", 
        "QueueId": "12345678", 
        "Title": "Some title here", 
        "Status": "21", 
        "Priority": "3", 
        "Source": "-2", 
        "TicketType": "4", 
        "IssueType": "21", 
        "SubIssueType": "303", 
        "Description": "Description of ticket", 
        "AssignedResourceID": "12345678", 
        "AssignedResourceRoleID": "23456789"
    }
"""

__version__ = 1.00
__author__ = "Wayne Kirk Schmidt (wayne.kirk.schmidt@changeis.co.jp)"

import json
import os
import sys
import argparse
import requests

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""
autotask_ticket creates a ticket in autotask from the data sent to it in JSON format
""")

PARSER.add_argument("-p", metavar='<password>', dest='my_password', \
                    help="specify password")
PARSER.add_argument("-u", metavar='<username>', dest='my_username', \
                    help="specify username")
PARSER.add_argument("-t", metavar='<tracking>', dest='my_tracking', \
                    help="specify tracking identifier")
PARSER.add_argument("-a", metavar='<apipoint>', dest='my_apipoint', \
                    help="specify API endpoint")
PARSER.add_argument("-j", metavar='<payload>', dest='my_jsonfile', \
                    help="specify JSON payload")

ARGS = PARSER.parse_args()

username = ARGS.my_username
password = ARGS.my_password
tracking = ARGS.my_tracking
endpoint = ARGS.my_apipoint
jsonfile = ARGS.my_jsonfile

if os.path.exists(jsonfile):
    with open( jsonfile, 'r', encoding='utf-8') as fileobject:
        payload = json.load(fileobject)

def main():
    """
    Drive for the ticket creation. 
    This takes a JSON file and outputs a URL or ticket number.
    """

    headers = {
        "username": username,
        "password": password,
        "integrationCode": tracking,
        "Content-Type": "application/json"
    }

    response = requests.request(method='POST', url=endpoint, \
        headers=headers, data=payload, timeout=1200, verify=False)

    print(response.status_code)

if __name__ == '__main__':
    main()
