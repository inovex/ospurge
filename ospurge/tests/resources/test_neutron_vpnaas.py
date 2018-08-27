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
import unittest

import shade

from ospurge.resources import neutron_vpnaas
from ospurge.tests import mock


class TestIpSecSiteConnections(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'conn1'}, {'name': 'conn2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      neutron_vpnaas.IpSecSiteConnections(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', return_value=self.client) as m:
            self.assertIsNone(
                neutron_vpnaas.IpSecSiteConnections(self.creds_manager).delete(sg))
            self.client.delete_ipsec_site_connection.assert_called_once_with(sg['id'])
    
    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("IPSec Site Connection (",
                      neutron_vpnaas.IpSecSiteConnections(self.creds_manager).to_str(sg))

class TestVPNServices(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_check_prerequisite(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=["conn1"]):
            self.assertEqual(
                False,
                neutron_vpnaas.VPNServices(self.creds_manager).check_prerequisite()
            )
        with mock.patch('shade.meta.get_and_munchify', return_value=[]):
            self.assertEqual(
                True,
                neutron_vpnaas.VPNServices(self.creds_manager).check_prerequisite()
            )

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'serv1'}, {'name': 'serv2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      neutron_vpnaas.VPNServices(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', return_value=self.client) as m:
            self.assertIsNone(
                neutron_vpnaas.VPNServices(self.creds_manager).delete(sg))
            self.client.delete_vpnservice.assert_called_once_with(sg['id'])
    
    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("VPN Service (",
                      neutron_vpnaas.VPNServices(self.creds_manager).to_str(sg))

class TestEndpointGroups(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_check_prerequisite(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=["conn1"]):
            self.assertEqual(
                False,
                neutron_vpnaas.EndpointGroups(self.creds_manager).check_prerequisite()
            )
        with mock.patch('shade.meta.get_and_munchify', return_value=[]):
            self.assertEqual(
                True,
                neutron_vpnaas.EndpointGroups(self.creds_manager).check_prerequisite()
            )

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'group1'}, {'name': 'group2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      neutron_vpnaas.EndpointGroups(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', return_value=self.client) as m:
            self.assertIsNone(
                neutron_vpnaas.EndpointGroups(self.creds_manager).delete(sg))
            self.client.delete_endpoint_group.assert_called_once_with(sg['id'])
    
    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("Endpoint Group (",
                      neutron_vpnaas.EndpointGroups(self.creds_manager).to_str(sg))


class TestIKEPolicies(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_check_prerequisite(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=["conn1"]):
            self.assertEqual(
                False,
                neutron_vpnaas.IKEPolicies(self.creds_manager).check_prerequisite()
            )
        with mock.patch('shade.meta.get_and_munchify', return_value=[]):
            self.assertEqual(
                True,
                neutron_vpnaas.IKEPolicies(self.creds_manager).check_prerequisite()
            )

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'policy1'}, {'name': 'policy2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      neutron_vpnaas.IKEPolicies(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', return_value=self.client) as m:
            self.assertIsNone(
                neutron_vpnaas.IKEPolicies(self.creds_manager).delete(sg))
            self.client.delete_ikepolicy.assert_called_once_with(sg['id'])
    
    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("IKE Policy (",
                      neutron_vpnaas.IKEPolicies(self.creds_manager).to_str(sg))

class TestIPSecPolicies(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_check_prerequisite(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=["conn1"]):
            self.assertEqual(
                False,
                neutron_vpnaas.IPSecPolicies(self.creds_manager).check_prerequisite()
            )
        with mock.patch('shade.meta.get_and_munchify', return_value=[]):
            self.assertEqual(
                True,
                neutron_vpnaas.IPSecPolicies(self.creds_manager).check_prerequisite()
            )

    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'policy1'}, {'name': 'policy2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      neutron_vpnaas.IPSecPolicies(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', return_value=self.client) as m:
            self.assertIsNone(
                neutron_vpnaas.IPSecPolicies(self.creds_manager).delete(sg))
            self.client.delete_ipsecpolicy.assert_called_once_with(sg['id'])
    
    @mock.patch('ospurge.resources.neutron_vpnaas.getNeutronClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("IPSec Policy (",
                      neutron_vpnaas.IPSecPolicies(self.creds_manager).to_str(sg))
