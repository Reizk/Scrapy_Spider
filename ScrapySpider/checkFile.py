from  ScrapySpider.items import EhentaiPageItem
import  requests
import  time
import os
from ScrapySpider.pipelines import  ScrapyspiderPipeline
from ScrapySpider.sqlite import sqlite
from  ScrapySpider.items import EhentaiPageItem
from  ScrapySpider.items import EhentaiBookItem
from  ScrapySpider.settings import ROOT_FILE

def CheckFile():
    pipeline= ScrapyspiderPipeline()
    s = sqlite()
    count=0
    r=s.fetchall(s.get_conn(ROOT_FILE+'spider.db'), '''SELECT * FROM EBP''')
    if(len(r)>0):
        for index in  range(len(r)):
            item=r[index]
            ebnumber= item[1]
            page=item[2]
            url=item[3]
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Accept': 'text/html,application/xhtml+xml,image/jxr, */*',
                       'Accept-Encoding': 'gzip,deflate',
                       'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3'
                       }
            # 待优化 下载失败等情况
            try:
                pic = requests.get(url, timeout=10, headers=headers)
                path = pipeline.root + str(ebnumber) + '\\' + str(page) + '.jpg'
                if not pipeline.isexists(path):
                    fp = open(path, 'wb')
                    fp.write(pic.content)
                    fp.close()
                    print("写入文件："+path)
                    time.sleep(0.1)
                    count=count-1
            except BaseException as e:
                print(e)
            count=count+1
    print(count)
CheckFile();