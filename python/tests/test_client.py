import unittest

from alibabacloud_fc_util.client import Client
from Tea.request import TeaRequest


class TestClient(unittest.TestCase):

    def test_get_content_md5(self):
        self.assertEqual("CY9rzUYh03PK3k6DJie09g==", Client.get_content_md5(
            bytes("test", encoding="utf-8")))

    def test_get_content_length(self):
        self.assertEqual(4, Client.get_content_length(
            bytes("test", encoding="utf-8")))

    def test_use(self):
        self.assertEqual("a", Client.use(True, "a", "b"))
        self.assertEqual("b", Client.use(False, "a", "b"))
        self.assertEqual("b", Client.use(None, "a", "b"))

    def test_get_signature(self):
        request = TeaRequest()
        request.pathname = "/test"
        request.method = "GET"
        signedStr = Client.get_signature(
            "accessKeyId", "accessKeySecret", request, "/version")
        self.assertEqual(
            "FC accessKeyId:tvvm2KiUDmXlQiuwz21CtN59JcKTT5QzIcrc122DKVo=", signedStr)

        header = {}
        header["x-fc-test"] = "test"
        request.headers = header
        signedStr = Client.get_signature(
            "accessKeyId", "accessKeySecret", request, "/version")
        self.assertEqual(
            "FC accessKeyId:lP6dXPCXlQNI7VY+f0brnZ4bwluNvGqcwdDf5GoM9ag=", signedStr)

        query = {}
        query["testQuery"] = "test"
        request.query = query
        request.pathname = "/version/proxy/"
        signedStr = Client.get_signature(
            "accessKeyId", "accessKeySecret", request, "/version")
        self.assertEqual(
            "FC accessKeyId:aCD88kzuMQYKQGo7kq7DeqhT72nVrNSEqAJtiHNj9L0=", signedStr)
