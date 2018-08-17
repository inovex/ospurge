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

class LoadBalancers(base.ServiceResource):
    ORDER = 47
        
    def getClient(self):
        authurl = os.environ.get("OS_AUTH_URL")
        user_name = os.environ.get("OS_USERNAME")
        pass_word = os.environ.get("OS_PASSWORD")
        if "OS_PROJECT_NAME" in os.environ:
            tenantname = os.environ.get("OS_PROJECT_NAME")
        else:
            tenantname = os.environ.get("OS_TENANT_NAME")
        apiversion = os.environ.get("OS_IDENTITY_API_VERSION")
        os_region_name = os.environ.get("OS_REGION_NAME")
        os_project_id=os.environ.get("OS_PROJECT_ID")

        auth = identity.V3Password(auth_url=authurl,
                               username=user_name,
                               user_domain_name='Default',
                               password=pass_word,
                               project_name=tenantname,
                               project_domain_name='Default')
        sess = session.Session(auth=auth) 
        network_client = self.cloud._get_raw_client('network')
        endpoint = network_client.get_endpoint()
        return octavia.OctaviaAPI(endpoint = endpoint, session=sess)

    def check_prerequisite(self):
        client = self.getClient()
        return meta.get_and_munchify('listeners', client.listener_list()) == [] and meta.get_and_munchify('pools', client.pool_list()) == []

    def list(self):
        client = self.getClient()
        return meta.get_and_munchify('loadbalancers', client.load_balancer_list())

    def delete(self, resource):
        client = self.getClient()
        try:
            client.load_balancer_delete(resource['id'])
        except Exception:
            traceback.print_exc()
            #pass

    @staticmethod
    def to_str(resource):
        return "VM (id='{}', name='{}')".format(
            resource['id'], resource['name'])

class Listeners(base.ServiceResource):
    ORDER = 41
        
    def getClient(self):
        authurl = os.environ.get("OS_AUTH_URL")
        user_name = os.environ.get("OS_USERNAME")
        pass_word = os.environ.get("OS_PASSWORD")
        if "OS_PROJECT_NAME" in os.environ:
            tenantname = os.environ.get("OS_PROJECT_NAME")
        else:
            tenantname = os.environ.get("OS_TENANT_NAME")
        apiversion = os.environ.get("OS_IDENTITY_API_VERSION")
        os_region_name = os.environ.get("OS_REGION_NAME")
        os_project_id=os.environ.get("OS_PROJECT_ID")

        auth = identity.V3Password(auth_url=authurl,
                               username=user_name,
                               user_domain_name='Default',
                               password=pass_word,
                               project_name=tenantname,
                               project_domain_name='Default')
        sess = session.Session(auth=auth) 
        network_client = self.cloud._get_raw_client('network')
        endpoint = network_client.get_endpoint()
        return octavia.OctaviaAPI(endpoint = endpoint, session=sess)

    def list(self):
        client = self.getClient()
        return meta.get_and_munchify('listeners', client.listener_list())

    def delete(self, resource):
        client = self.getClient()
        try:
            client.listener_delete(resource['id'])
        except Exception:
            traceback.print_exc()
            #pass

    @staticmethod
    def to_str(resource):
        return "VM (id='{}', name='{}')".format(
            resource['id'], resource['name'])

class Pools(base.ServiceResource):
    ORDER = 40
        
    def getClient(self):
        authurl = os.environ.get("OS_AUTH_URL")
        user_name = os.environ.get("OS_USERNAME")
        pass_word = os.environ.get("OS_PASSWORD")
        if "OS_PROJECT_NAME" in os.environ:
            tenantname = os.environ.get("OS_PROJECT_NAME")
        else:
            tenantname = os.environ.get("OS_TENANT_NAME")
        apiversion = os.environ.get("OS_IDENTITY_API_VERSION")
        os_region_name = os.environ.get("OS_REGION_NAME")
        os_project_id=os.environ.get("OS_PROJECT_ID")

        auth = identity.V3Password(auth_url=authurl,
                               username=user_name,
                               user_domain_name='Default',
                               password=pass_word,
                               project_name=tenantname,
                               project_domain_name='Default')
        sess = session.Session(auth=auth) 
        network_client = self.cloud._get_raw_client('network')
        endpoint = network_client.get_endpoint()
        return octavia.OctaviaAPI(endpoint = endpoint, session=sess)

    def list(self):
        client = self.getClient()
        return meta.get_and_munchify('pools', client.pool_list())

    def delete(self, resource):
        client = self.getClient()
        try:
            client.pool_delete(resource['id'])
        except Exception:
            traceback.print_exc()
            #pass

    @staticmethod
    def to_str(resource):
        return "VM (id='{}', name='{}')".format(
            resource['id'], resource['name'])



