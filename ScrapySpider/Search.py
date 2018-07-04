from ScrapySpider.sqlite import sqlite
from  ScrapySpider.settings import ROOT_FILE
s=sqlite()
s.fetchall(s.get_conn(ROOT_FILE+'spider.db'), '''SELECT * FROM EB''')
s.fetchall(s.get_conn(ROOT_FILE+'spider.db'), '''SELECT * FROM EBP''')