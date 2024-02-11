# coding: utf-8

from __future__ import absolute_import
from tests import BaseTestCase
import unittest


class BaseTestAliveController(BaseTestCase):
    def test_get_restful(self):
        
        _id = "test1"
        
        # Delete Item
        response = self.client.open("/api/db/{}".format(_id), method="DELETE")
      
        sample_payload = {
            "id": _id,
            "name": _id
        }
        
        # Create Item
        response = self.client.open("/api/db", json=sample_payload, method="POST")
        print('response - ', response)
        print('response.status_code - ', response.status_code)
        assert response.status_code == 201
     
        response = self.client.open("/api/db", method="GET")
        self.assert200(response)
        assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()