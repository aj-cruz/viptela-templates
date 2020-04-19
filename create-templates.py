"""
Create various Viptela feature templates on a vManage.
To maximize reusability of templates I made most platform dependent settings
variables, such as interface names.
The raw (JSON format) templates are in the payloads folder.
The raw JSON templates can be modified as you see fit for your deployment, or
modified via GUI after creation.
As you peruse the raw templates you'll notice a "vipType" key for every section
of configuration. There are three vipType's you should be aware of:
    1. ignore (this sets the value to the Viptela default)
    2. constant (this sets the value to a global value you provide)
    3. variableName (this sets the value to a variable to be provided later)

The script is indempotent based on template name. If the template name already
exists, the POST for that template will not make any changes to the environment.

Tested on the following vManage versions:
    18.4.4

aj.cruz@pivotts.com
"""

import getpass
import requests
import sys
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from payloads import (
    payload_global_system_template,
    payload_ntp,
    payload_ospf_hub,
    payload_omp,
    payload_vpn0,
    payload_vpn0_inet,
    payload_vpn0_mpls,
    payload_vpn10,
    payload_vpn10_hub_int,
    payload_loopback0_int,
    payload_lan_trunk_int,
    payload_lan_data_int,
    payload_lan_voice_int,
    payload_vpn512,
    payload_vpn512_int,
    payload_vpn90
)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        try:
            self.login(self.vmanage_ip, username, password)
        except:
            print("\n\nLog in failed, exiting\n\n")
            sys.exit()

    def login(self, vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = 'https://{}/'.format(vmanage_ip)
        login_action = '/j_security_check'
        #Format data for loginForm
        login_data = {'j_username' : username, 'j_password' : password}
        #Url for posting login data
        login_url = base_url_str + login_action
        url = base_url_str + login_url
        sess = requests.session()
        #If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)
        if b"html" in login_response.content:
            sys.exit()
        else:
            self.session[vmanage_ip] = sess

    # get_request isn't used in this script, I just left it in for reference in case I want to use it later
    def get_request(self, mount_point):
        """GET request"""
        url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
        print(url)
        response = self.session[self.vmanage_ip].get(url, verify=False).json()
        data = response
        return data

    def post_request(self, mount_point, payload, headers={'Content-Type': 'application/json'}):
        """POST request"""
        url = "https://{}:8443/dataservice/{}".format(self.vmanage_ip, mount_point)
        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        if not response.status_code == 200:
            results = json.loads(response.content)
            print("Error {}: {}".format(results['error']['code'],results['error']['message']))
            print('{}\n'.format(results['error']['details']))
        else:
            print('SUCCESS\n')
            data = response.content
            return data


if __name__ == "__main__":
    # Get vManage info & credentials
    vmanage_hostname = input('\n\nvManage Hostname/IP Address: ')
    username = input('Username: ')
    password = getpass.getpass(prompt='Password: ')

    # Log in and create the session object
    obj = rest_api_lib(vmanage_hostname, username, password)

    # Create Global System Template
    print('\nCreating Global System Template')
    payload = payload_global_system_template.data().payload
    obj.post_request('template/feature/', payload)

    # Create Global NTP Template
    print('\nCreating Global NTP Template')
    payload = payload_ntp.data().payload
    obj.post_request('template/feature/', payload)

    # Create Global VPN512 Template
    print('\nCreating Global VPN512 Template')
    payload = payload_vpn512.data().payload
    obj.post_request('template/feature/', payload)

    # Create Global VPN512 (Mgmt Interface) Template
    print('\nCreating Global VPN512 Interface Template')
    payload = payload_vpn512_int.data().payload
    obj.post_request('template/feature/', payload)

    # Create Global OMP Template (Enable OSPF External Redistribution)
    print('\nCreating Global OMP Template')
    payload = payload_omp.data().payload
    obj.post_request('template/feature/', payload)

    # Create VPN0 Template
    print('\nCreating VPN0 Template')
    payload = payload_vpn0.data().payload
    obj.post_request('template/feature/', payload)

    # Create VPN0 Internet Interface Template
    print('\nCreating VPN0 Internet Interface Template')
    payload = payload_vpn0_inet.data().payload
    obj.post_request('template/feature/', payload)

    # Create VPN0 MPLS Interface Template
    print('\nCreating VPN0 MPLS Interface Template')
    payload = payload_vpn0_mpls.data().payload
    obj.post_request('template/feature/', payload)

    # Create VPN10 (Corporate) Template
    print('\nCreating CORP VPN (10) Template')
    payload = payload_vpn10.data().payload
    obj.post_request('template/feature/', payload)

    # Create VPN10 (Corporate) Hub Interface Template
    print('\nCreating VPN10 Hub Interface Template')
    payload = payload_vpn10_hub_int.data().payload
    obj.post_request('template/feature/', payload)

    # Create Loopback0 Interface Template
    print('\nCreating Loopback0 Interface Template')
    payload = payload_loopback0_int.data().payload
    obj.post_request('template/feature/', payload)

    # Create OSPF Template for Hub routers
    print('\nCreating OSPF Hub Template')
    payload = payload_ospf_hub.data().payload
    obj.post_request('template/feature/', payload)

    # Create LAN Trunk Physical Interface Template
    print('\nCreating LAN Physical Trunk Interface Template')
    payload = payload_lan_trunk_int.data().payload
    obj.post_request('template/feature/', payload)

    # Create LAN Data Interface Template
    print('\nCreating LAN Data Interface Template')
    payload = payload_lan_data_int.data().payload
    obj.post_request('template/feature/', payload)

    # Create LAN Voice Interface Template
    print('\nCreating LAN Voice Interface Template')
    payload = payload_lan_voice_int.data().payload
    obj.post_request('template/feature/', payload)

    # Create VPN90 (PCI) Template
    print('\nCreating PCI VPN (90) Template')
    payload = payload_vpn90.data().payload
    obj.post_request('template/feature/', payload)
