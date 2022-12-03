import unittest
import requests
import os,sys
import json
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data



class MyTestCase(unittest.TestCase):
    def setUp(self):
        headers = {"Content-Type": "application/json;charset=utf8"}
        url = "http://120.77.215.105/prod-api/auth/login"
        _data = {
            "username": "admin",
            "password": "admin123"
        }
        res = requests.post(url=url, headers=headers, json=_data).text
        res = json.loads(res)
        self.token = res["data"]["access_token"]
        self.base_url="http://120.77.215.105/prod-api/system/user/list?pageNum=1&pageSize=10&userName=ad"

    def tearDown(self) :
        print(self.result)

    def test_user(self):
        headers = {"Content-Type": "application/json;charset=utf8","Authorization":self.token}
        r=requests.get(url=self.base_url,headers=headers).text
        self.result = json.loads(r)
        self.assertEqual(self.result['code'],200)

    def test_user2(self):
        headers = {"Content-Type": "application/json;charset=utf8","Authorization":self.token}
        r=requests.get(url=self.base_url,headers=headers).text
        self.result = json.loads(r)
        self.assertEqual(self.result['code'],200)








if __name__ == '__main__':
    #test_data.init_data()  # 初始化接口测试数据
    unittest.main()

