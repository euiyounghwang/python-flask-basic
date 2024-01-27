# coding: utf-8

from __future__ import absolute_import
from tests import BaseTestCase
import unittest


class BaseTestAliveController(BaseTestCase):
    def test_get_restful(self):
        response = self.client.open("/api/db", method="GET")
        self.assert200(response)
        assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()