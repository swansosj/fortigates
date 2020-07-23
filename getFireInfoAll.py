import requests
import pprint
import openpyxl
import os
from getpass import getpass


#USER = input("Enter your username: ")
#PASS = getpass()


FORTIGATES = [
    {'name':'ARGCRPFW','mgmtIP':'200.3.195.7'},
    {'name':'ATLCRPPRDFW','mgmtIP':'209.17.114.90'},
    {'name':'ATLPRD1SCFW','mgmtIP':'209.17.114.76'},
    {'name':'ATLRPRDFWA','mgmtIP':'209.17.114.95'},
    {'name':'ATLPRDACQFW','mgmtIP':'209.17.114.91'},
    {'name':'ATLPRDFWECOM','mgmtIP':'209.17.114.75'},
    {'name':'ATL4PRDFWOOB','mgmtIP':'206.188.199.55'},
    {'name':'ATL4PRDFWVPN','mgmtIP':'209.17.114.93'},
    {'name':'ATLPRDFWVPNB','mgmtIP':'209.17.114.94'},
    {'name':'ATLPRDFWVUX','mgmtIP':'209.17.114.78'},
    {'name':'ATLPRDFWWIN','mgmtIP':'209.17.114.79'},
    {'name':'ATLCRPGUESTFW','mgmtIP':'192.168.6.9'},
    {'name':'CDFUKFW','mgmtIP':'213.104.102.10'},
    {'name':'HFXCRPFW','mgmtIP':'205.178.155.10'},
    {'name':'HRNCRPFW','mgmtIP':'192.84.39.5'},
    {'name':'HYDFW','mgmtIP':'14.98.171.122'},
    {'name':'HZLCRPFW','mgmtIP':'205.178.130.14'},
    {'name':'JAXCRPPRDFW','mgmtIP':'64.69.216.78'},
    {'name':'JAXDEVQAFW','mgmtIP':'64.69.216.67'},
    {'name':'JAXPRDFWOOB','mgmtIP':'173.224.64.172'},
    {'name':'JAXPRDFWVPN','mgmtIP':'64.69.216.77'},
    {'name':'JAXPRDPCIFW','mgmtIP':'10.40.0.4'},
    {'name':'JAXHQFW','mgmtIP':'10.70.0.10'},
    {'name':'JAXPRDFWA','mgmtIP':'64.69.217.133'},
    {'name':'NGWCRPFW','mgmtIP':'205.178.154.10'},
    {'name':'PDXCRPFW','mgmtIP':'205.178.180.10'},
    {'name':'JAXPRDFWVPNA','mgmtIP':'10.40.100.78'},
    {'name':'SGHCRPFW','mgmtIP':'97.65.11.242'},
]

wb = openpyxl.load_workbook('fireresults.xlsx')
sheet = wb.active
COUNT = 2

for fire in FORTIGATES:
    print("Starting " + fire['name'])
    urlogin = "https://" + fire['mgmtIP'] + "/logincheck"
    #payload = "username=" + USER + "&secretkey=" + PASS
    payload = "username=wclark&secretkey=XinZ%m#E*Mt4FW"
    headers = {'Content-Type': 'application/json'}
    requests.packages.urllib3.disable_warnings()
    response = requests.request("POST", urlogin, headers=headers, data=payload, verify=False)
    cookie = response.headers['Set-Cookie']
    urladdr = "https://" + fire['mgmtIP'] + ":443/api/v2/monitor/system/firmware"
    payload2 = {}
    authheaders = {'Cookie':cookie}
    sysresponse = requests.request("GET", urladdr, headers=authheaders, data=payload2, verify=False)
    sysJSON = sysresponse.json()
    version = sysJSON['version']
    sheet['A' + str(COUNT)] = fire['name']
    sheet['B' + str(COUNT)] = fire['mgmtIP']
    sheet['C' + str(COUNT)] = version
    COUNT = COUNT + 1
    print(COUNT)

print('Saving....')
wb.save('fireresulttest.xlsx')
print('Complete')
