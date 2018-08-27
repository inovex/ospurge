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
from octaviaclient.api.v2 import octavia
from keystoneauth1 import identity
from keystoneauth1 import session
from shade import meta
import os
import traceback
from neutronclient.v2_0 import client


# shade does not have any functions for handling loadbalancers 
# so we have to work on the "barebones" client
def getOctaviaClient(options):
        authurl = options.os_auth_url
        user_name = options.os_username
        pass_word = options.os_password
        #tenant name and project name is the same thing
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
        return octavia.OctaviaAPI(endpoint = network_client.get_auth_info()['endpoint_url'], session=sess)

class LoadBalancers(base.ServiceResource):
    ORDER = 47

    def check_prerequisite(self):
        client = getOctaviaClient(self.options)
        return meta.get_and_munchify('listeners', client.listener_list()) == [] and meta.get_and_munchify('pools', client.pool_list()) == []

    def list(self):
        client = getOctaviaClient(self.options)
        return meta.get_and_munchify('loadbalancers', client.load_balancer_list())

    def delete(self, resource):
        client = getOctaviaClient(self.options)
        client.load_balancer_delete(resource['id'])

    @staticmethod
    def to_str(resource):
        return "Load Balancer (id='{}', name='{}')".format(
            resource['id'], resource['name'])

class Listeners(base.ServiceResource):
    ORDER = 41

    def check_prerequisite(self):
        client = getOctaviaClient(self.options)
        return meta.get_and_munchify('pools', client.pool_list()) == []

    def list(self):
        client = getOctaviaClient(self.options)
        return meta.get_and_munchify('listeners', client.listener_list())

    def delete(self, resource):
        client = getOctaviaClient(self.options)
        client.listener_delete(resource['id'])

    @staticmethod
    def to_str(resource):
        return "Listener (id='{}', name='{}')".format(
            resource['id'], resource['name'])

class Pools(base.ServiceResource):
    ORDER = 40
        
    def list(self):
        client = getOctaviaClient(self.options)
        return meta.get_and_munchify('pools', client.pool_list())

    def delete(self, resource):
        client = getOctaviaClient(self.options)
        client.pool_delete(resource['id'])

    @staticmethod
    def to_str(resource):
        return "Pool (id='{}', name='{}')".format(
            resource['id'], resource['name'])



