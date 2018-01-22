#coding=utf-8
import json
import unittest
import requests
import sys
from util import logincookies
from util import util

class TestEamEqut(unittest.TestCase):
    def setUp(self):
        self.cookie=logincookies.geteamcookie()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
                   "Accept": "application/json, text/javascript, */*; q=0.01",
                   "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                   "Accept-Encoding": "gzip, deflate",
                   "Connection": "keep-alive",
                   "Upgrade-Insecure-Requests": "1",
                   }
    def tearDown(self):
        pass

    def test_001_eamequtsave(self):
        url = 'http://yfb-eam.hd-cloud.com/eam/EAM_EQUT/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=EAM_EQUT&0.46442153106909034&contentType=json&ajax=true'
        # print(sys._getframe().f_code.co_name)
        r = requests.post(url, headers=self.headers, json=util.readjson("eamequtsave"), cookies=self.cookie)
        print(r.text)

    '''设备台账保存数据'''


if __name__ == '__main__':
    unittest.main()


