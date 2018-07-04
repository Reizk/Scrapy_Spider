# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  ScrapySpider.items import EhentaiPageItem
import  requests
import  time
import os

from ScrapySpider.sqlite import sqlite
from  ScrapySpider.items import EhentaiPageItem
from  ScrapySpider.items import EhentaiBookItem
from  ScrapySpider.settings import ROOT_FILE
class ScrapyspiderPipeline(object):
    def isexists(self,path):
        return  os.path.exists(path)
    def mkdir(self,path):
        # 引入模块
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录

            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在

            return False
    def __init__(self):
        self.sqlite=sqlite()
        self.root = ROOT_FILE
        CreateEBSql = '''Create table if not exists  'EB'
        ('booknumber' int (11) Not Null,
        'title' varchar(200) not Null,
        'url' varchar(200) not Null,
        'tag' varchar(2048) DEFAULT NULL,
        primary key('booknumber')
        )
        '''
        CreateEBPSql = '''Create table if not exists  'EBP'
        ('booknumberAddPage' varchar(50) Not Null,
        'booknumber' int (11) Not Null,
        'page' int(11) not Null,
        'url' varchar(200) not Null,
        primary key('booknumberAddPage')
        )
        '''
        self.sqlite.create_table(self.sqlite.get_conn(self.root+'spider.db'),CreateEBSql)
        self.sqlite.create_table(self.sqlite.get_conn(self.root+'spider.db'),CreateEBPSql)
    def process_item(self, item, spider):
        if(type(item) is EhentaiBookItem):
            save_sql='''insert or ignore into EB values(?,?,?,?)'''
            data=[(item['booknumber'],item['title'],item['url'],item['tag'])]
            self.sqlite.save(self.sqlite.get_conn(self.root+'spider.db'),save_sql,data)
        if(type(item) is EhentaiPageItem):
            save_sql = '''insert or ignore into EBP values(?,?,?,?)'''
            data = [(item['booknumber']+"_"+item['pagenumber'], item['booknumber'], item['pagenumber'], item['url'])]
            self.sqlite.save(self.sqlite.get_conn(self.root + 'spider.db'), save_sql, data)
            rootpath=self.root+item['booknumber']
            self.mkdir(rootpath)
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Accept': 'text/html,application/xhtml+xml,image/jxr, */*',
                       'Accept-Encoding': 'gzip,deflate',
                       'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3'
                       }
            #待优化 下载失败等情况

            pic = requests.get(item['url'],timeout=10, headers=headers)
            path =self.root+item['booknumber']+'\\' + item['pagenumber'] + '.jpg'
            if not self.isexists(path):
                fp = open(path, 'wb')
                fp.write(pic.content)
                fp.close()
                time.sleep(0.05)

