#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
from ospurge.resources import base
import logging
import os
from keystoneauth1 import identity
from keystoneauth1 import session
from shade import meta
from neutronclient.v2_0 import client


# shade does not have any functions for handling VPN resources 
# so we have to work on the "barebones" Neutron client
def getNeutronClient(options):
        authurl = options.os_auth_url
        user_name = options.os_username
        pass_word = options.os_password
        try:
            tenantname = options.os_project_name
        except AttributeError:
            tenantname = options.os_tenant_name
        os_region_name = options.os_region_name
        os_project_id = options.os_project_id

        auth = identity.V3Password(auth_url=authurl,
                               username=user_name,
                               user_domain_name='Default',
                               password=pass_word,
                               project_name=tenantname,
                               project_domain_name='Default')
        sess = session.Session(auth=auth) 
        network_client = client.Client(session=sess)
        return network_client

class IpSecSiteConnections(base.ServiceResource):
    ORDER = 26

    def list(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ipsec_site_connections', client.list_ipsec_site_connections())

    def delete(self, resource):
        client = getNeutronClient(self.options)
        client.delete_ipsec_site_connection(resource['id'])

    @staticmethod
    def to_str(resource):
        return "IPSec Site Connection (id='{}')".format(resource['id'])


class VPNServices(base.ServiceResource):
    ORDER = 27

    def check_prerequisite(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ipsec_site_connections', client.list_ipsec_site_connections()) == []

    def list(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('vpnservices', client.list_vpnservices())

    def delete(self, resource):
        client = getNeutronClient(self.options)
        client.delete_vpnservice(resource['id'])

    @staticmethod
    def to_str(resource):
        return "VPN Service (id='{}')".format(resource['id'])


class EndpointGroups(base.ServiceResource):
    ORDER = 28

    def check_prerequisite(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ipsec_site_connections', client.list_ipsec_site_connections()) == []

    def list(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('endpoint_groups', client.list_endpoint_groups())

    def delete(self, resource):
        client = getNeutronClient(self.options)
        client.delete_endpoint_group(resource['id'])

    @staticmethod
    def to_str(resource):
        return "Endpoint Group (id='{}')".format(resource['id'])


class IKEPolicies(base.ServiceResource):
    ORDER = 29

    def check_prerequisite(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ipsec_site_connections', client.list_ipsec_site_connections()) == []

    def list(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ikepolicies', client.list_ikepolicies())

    def delete(self, resource):
        client = getNeutronClient(self.options)
        client.delete_ikepolicy(resource['id'])

    @staticmethod
    def to_str(resource):
        return "IKE Policy (id='{}')".format(resource['id'])

class IPSecPolicies(base.ServiceResource):
    ORDER = 30

    def check_prerequisite(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ipsec_site_connections', client.list_ipsec_site_connections()) == []

    def list(self):
        client = getNeutronClient(self.options)
        return meta.get_and_munchify('ipsecpolicies', client.list_ipsecpolicies())

    def delete(self, resource):
        client = getNeutronClient(self.options)
        client.delete_ipsecpolicy(resource['id'])

    @staticmethod
    def to_str(resource):
        return "IPSec Policy (id='{}')".format(resource['id'])
