import requests
import pprint
import os
import openpyxl
from getpass import getpass


USER = input("Enter your username: ")
PASS = getpass()

IP = []
FQDN = []
RANG = []
DUPLICATES = []

JAXHQFW = {'name':'JAXHQFW','mgmt':'10.70.0.10'}

urlogin = "https://" + JAXHQFW['mgmt'] + "/logincheck"
payload = "username=" + USER + "&secretkey=" + PASS
requests.packages.urllib3.disable_warnings()
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", urlogin, headers=headers, data = payload, verify=False)
cookie = response.headers['Set-Cookie']
urladdr = "https://" + JAXHQFW['mgmt'] + ":443/api/v2/monitor/system/firmware"
payload2 = {}
authheaders = {'Cookie':cookie}
response1 = requests.request("GET", urladdr, headers=authheaders, data=payload2, verify=False)
#print(response1)
sysobj = response1.json()
version = sysobj['version']
print(version)
