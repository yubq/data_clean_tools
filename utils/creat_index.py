# -*- coding:utf-8 -*-
# @Time    :20222022/8/29下午5:11
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

from elasticsearch import Elasticsearch


class python2es:
    def __init__(self):
        self.es = Elasticsearch('127.0.0.1:9200')

    def guide_mapping(self):
        body = {
            "mapping":{
                "properties":{
                    "firstword":{
                        "type":"keywprds"
                    },
                    "lastword":{
                        "type":"text",
                        "analyzer":"ik_max_word"
                    }
                }
            }
        }
        self.es.indices.create(index="data_guide",body=body)

    def creat_data_mapping(self):
        body = {
            "mapping":{
                "properties":{
                    "filter_name":{
                        "type":"text",
                        "analyzer":"ik_max_word",
                        "search_analyzer":"ik_max_word"
                    },
                    "level_name":{
                        "type":"text",
                        "fields":{
                            "keywords":{
                                "type":"keywords",
                                "ignore_above":256
                            }
                        }
                    },
                    "level_code":{
                        "type":"text"
                    }
                }
            }
        }
        self.es.indices.create(index="data_mapping",body=body)
        return True

    def creat_sync_mapping(self):
        body = {
            "settings":{
                "analysis":{
                    "filter":{
                        "wprd_sync":{
                            "type":"synonym_graph",
                            "synonyms_path":"ananlysis/sys_word.txt"
                            # "updateable":True
                        }
                    },
                    "analyzer":{
                        "ik_sysc_smart":{
                            "filter":["word_sysc"],
                            "type":"custom",
                            "tokenizer":"ik_smart"
                        }
                    }
                }
            },
            "mapping":{
                "properties":{
                    "business_name":{
                        "type":"text",
                        "analyzer":"ik_sync_smart"
                    }
                }
            }
        }
        self.es.indices.create(index="business",body=body)
        return True

    def delete_inde(self,index):
        self.es.indices.delete(index=index)
        return True

    def delete_info(self,index,body):
        self.es.delete_by_query(index=index,body=body)
        return True




































