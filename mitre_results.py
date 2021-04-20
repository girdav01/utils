# David Girard Sr Product Manager Trend Micro
# Get MITRE Evaluation #3 raw json results
# April 20th 2021
import requests

base_url = "https://attackevals.mitre-engenuity.org/downloadable_JSON/"
suffix = "_Results.json"
vendors = ['AhnLab','Bitdefender', 'CheckPoint', 'Cisco', 'CrowdStrike', 'Cyberreason', 'CyCraft', 'Cylance',
           'Cynet', 'Elastic','ESET', 'Fidelis', 'FireEye', 'Fortinet','F-Secure', 'GoSecure', 'Malwarebytes',
           'McAfee', 'MicroFocus', 'Microsoft', 'OpenText', 'PaloAltoNetworks', 'ReaQta', 'SentinelOne',
           'Sophos', 'Symantec', 'TrendMicro', 'Uptycs', 'VMware']

def getResults(v):
    print(v+suffix)
    r_file = requests.get(base_url + v + suffix)
    with open('data/' + v+suffix, 'w') as f:
        f.write(r_file.text)

for vendor in vendors:
    getResults(vendor)
