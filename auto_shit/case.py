# -*-coding:utf8-*-
import unittest
import requests

class Testhttp(unittest.TestCase):
    def setUp(self):
        print 'start'

    def tearDown(self):
        print 'end'

    def test_http(self):
        url = 'http://cs-common.vmceshi.com/storage?catalog=kmelearning:introduction&key=lianning'
        result = requests.get(url=url)
        self.assertEqual(result, result)
    def test_http2(self):
        url = 'http://cs-common.vmceshi.com/storage'
        jsondata = {  "catalog":"4","key":"4","introduction":"打南边来了个喇嘛","socre":"100","rank":"1","jointime":"2017-05-17"	}
        result = requests.post(url=url,json=jsondata)
        self.assertEqual(result, result)

    def test_http3(self):
        url = "http://cs-common.vmceshi.com/storage?catalog=kmelearning:introduction&key=lianning2"
        jsondata = {"introduction": "100","socre": "100","rank": "1","jointime": "2017-05-16"}
        result = requests.put(url=url,json=jsondata)
        self.assertEqual(result, result)

if __name__ == '__main__':
    unittest.main()
