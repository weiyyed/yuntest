#coding=utf-8
import json
import unittest
import requests
import logincookies
"""dd"""
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
        with open(r"...\testdata\eamequtsave.json",'r',encoding='utf-8') as es:
            self.eamequtsave=json.load(es)
    def tearDown(self):
        pass

    def test_001_eamequtsave(self):
        url = 'http://yfb-eam.hd-cloud.com/eam/EAM_EQUT/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=EAM_EQUT&0.46442153106909034&contentType=json&ajax=true'

        # jsondata = '{"tableName":"eam_equt","equt_scrap_age":"10","equt_run_time":17724,"dataStatus":0,"ver":1,"created_by":null,"created_dt":"2018-01-09 12:57:11","updated_by":null,"updated_dt":"2018-01-09 12:57:11","df":0,"tenantid":10000000550,"ts":null,"equt_class__name":"设备分类01","equt_class":"1","equt_professional":"01","equt_abc_type":"A","equt_state":"ON","equt_good_state":"01","equt_ext_type":null,"equt_asset_state":null,"equt_qr_code":null,"status":null,"equt_size":null,"equt_name":"自动设备名称001","equt_locationnum":"weihao001","equt_model":"xinghao001","equt_owner_dept__name":"海顿测试","equt_owner_dept":"hdtest","orgid":10000005008}'
        # bodydata=json.loads(jsondata)
        # print(bodydata)
        r = requests.post(url,headers=self.headers,json=self.eamequtsave,cookies=self.cookie)
        print(r.text)

    '''设备台账保存数据'''


if __name__ == '__main__':
    unittest.main()


