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

from ospurge.resources import octavia
from ospurge.tests import mock


class TestLoadBalancers(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_check_prerequisite(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=["LB1"]):
            self.assertEqual(
                False,
                octavia.LoadBalancers(self.creds_manager).check_prerequisite()
            )
        with mock.patch('shade.meta.get_and_munchify', return_value=[]):
            self.assertEqual(
                True,
                octavia.LoadBalancers(self.creds_manager).check_prerequisite()
            )


    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'LB1'}, {'name': 'LB2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      octavia.LoadBalancers(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.octavia.getOctaviaClient', return_value=self.client) as m:
            self.assertIsNone(
                octavia.LoadBalancers(self.creds_manager).delete(sg))
            self.client.load_balancer_delete.assert_called_once_with(sg['id'])
    
    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("Load Balancer (",
                      octavia.LoadBalancers(self.creds_manager).to_str(sg))

class TestListeners(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()


    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_check_prerequisite(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=["Listener1"]):
            self.assertEqual(
                False,
                octavia.Listeners(self.creds_manager).check_prerequisite()
            )
        with mock.patch('shade.meta.get_and_munchify', return_value=[]):
            self.assertEqual(
                True,
                octavia.Listeners(self.creds_manager).check_prerequisite()
            )

    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'Listener1'}, {'name': 'Listener2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      octavia.Listeners(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.octavia.getOctaviaClient', return_value=self.client) as m:
            self.assertIsNone(
                octavia.Listeners(self.creds_manager).delete(sg))
            self.client.listener_delete.assert_called_once()
    
    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("Listener (",
                      octavia.Listeners(self.creds_manager).to_str(sg))

class TestPools(unittest.TestCase):
    def setUp(self):
        self.cloud = mock.Mock(spec_set=shade.openstackcloud.OpenStackCloud)
        self.creds_manager = mock.Mock(cloud=self.cloud)
        self.client = mock.MagicMock()

    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_list(self):
        with mock.patch('shade.meta.get_and_munchify', return_value=[{'name': 'Pool1'}, {'name': 'Pool2'}]):
            self.assertIs(shade.meta.get_and_munchify.return_value,
                      octavia.Pools(self.creds_manager).list())

    def test_delete(self):
        sg = mock.MagicMock()
        with mock.patch('ospurge.resources.octavia.getOctaviaClient', return_value=self.client) as m:
            self.assertIsNone(
                octavia.Pools(self.creds_manager).delete(sg))
            self.client.pool_delete.assert_called_once()
    
    @mock.patch('ospurge.resources.octavia.getOctaviaClient', mock.Mock())
    def test_to_string(self):
        sg = mock.MagicMock()
        self.assertIn("Pool (",
                      octavia.Pools(self.creds_manager).to_str(sg))

