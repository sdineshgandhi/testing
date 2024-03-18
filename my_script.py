import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s=requests.Session()
s.verify=False

vcip=blrdcvc7.radisys.com
username=dsivaram@radisys.com
password='G00dLuckd$'
post(https://vcip/api/session,basic_auth=(username,password))