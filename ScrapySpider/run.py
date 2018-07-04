from scrapy import  cmdline


name='Ehentai'

cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())