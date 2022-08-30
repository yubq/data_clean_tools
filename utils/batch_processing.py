# -*- coding:utf-8 -*-
# @Time    :20222022/8/30上午9:56
# @Author  : yubq
# @Software: PyCharm
# @Software: PyCharm
'''
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               佛祖保佑       永无BUG
            十年生死两茫茫，写程序，到天亮。
               千行代码，Bug何处藏。
            纵使上线又怎样，朝令改，夕断肠。
            
            领导每天新想法，天天改，日日忙。
               相顾无言，惟有泪千行。
            每晚灯火阑珊处，夜难寐，加班狂。
'''
import datetime
from elasticsearch import Elasticsearch


es = Elasticsearch("127.0.0.1:9200")


def check_id(idnum):
    gender_id = {"0": "女", "1": "男"}

    verification = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    final_dict = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8,5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
    if len(str(idnum)) == 18:
        num_sum = 0
        for i, j in zip(list(idnum)[0:17],verification):
            num_sum += int(i)*j
        if str(final_dict[num_sum%11]) == str(idnum[17]).upper():
            sex = gender_id[str(int(idnum[14:17])%2)]
            birth = idnum[6:10] + '-' + idnum[10:12] + '-' + idnum[12:14]
            age = int(datetime.datetime.now().year) - int((idnum[6:10]))
            response = {"sex": sex, "birth": birth, "age": age}
        else:
            response = "证件信息输入有误"
    else:
        response = "数据长度不符合规范"
    return response



def search_data_batch(query):
    body = {
        "query": {
            "match": {
                "mergename": query
            }
        },
        "_source":['','',''],
        "from": 0,
        "size": 10
    }
    res = es.search(index='test',body=body)
    try:
        data_res =res['hits']['hits'][0]['_source']
        data_res = res['hits']['hits']
        test_name = '@'.join([str(i["_source"]['test_name']) for i in data_res])
    except Exception as e:
        test_name = "待补充"
    return test_name





