# -*- coding:utf-8 -*-
# @Time    :20222022/8/29下午5:00
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
import cx_Oracle as cx


class py2oracle:
    def __init__(self):
        self.con = cx.connect()
        self.cursor = self.con.cursor()

    def search_data(self,sql):
        res = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def insert_data(self,sql):
        try:
            self.cursor.execute(sql)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            return e

    def insert_manydata(self,sql,data):
        try:
            self.cursor.executemany(sql,data)
            self.con.commit()
            return True
        except Exception as e:
            self.con.rollback()
            return e

    def __del__(self):
        if hasattr(self,'cursor'):
            self.cursor.close()
        if hasattr(self,'con'):
            self.con.close()