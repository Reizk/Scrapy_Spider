import scrapy
import re
from scrapy.http import Request
from ScrapySpider.items import  EhentaiPageItem
from ScrapySpider.items import EhentaiBookItem
class EhentaiSpider(scrapy.Spider):
    name = "Ehentai"
    allowed_domains=["e-hentai.org"]
    start_urls =set([


'https://e-hentai.org/lofi/g/Xxx/xxx/' ,


                  ])
    def Re(self,text):
        p2 = r"(?<=<a href=\").+?(?=\")"
        pattern2 = re.compile(p2)
        return pattern2.findall(text)
    def RePicLink(self,text):
        p2 = r"(?<=src=\").+?(?=\")"
        pattern2 = re.compile(p2)
        return pattern2.findall(text)

    def ReTitle(self,text):
        p=r"(?<=<title>).+?(?=<\/title>)"
        pattern=re.compile(p)
        return pattern.findall(text)
    def ReTag(self,text):
        p=r"(?<=content=\"Tags:).+?(?=\")"
        pattern=re.compile(p)
        return pattern.findall(text)
    def start_requests(self):

        for url in self.start_urls:
            yield self.make_requests_from_url(url)




    def parse(self, response):
        text= response.text
        if response.url.startswith('https://e-hentai.org/lofi/g'):
           item=EhentaiBookItem()
           item['url']=response.url
           item['booknumber']= response.url.split('/')[5]
           item['title']=self.ReTitle(text)[0]
           item['tag']=self.ReTag(text)[0]
           yield item
           for url in self.Re(text):
               yield Request(url,callback=self.parse)
        if response.url.startswith('https://e-hentai.org/lofi/s'):
            for url in self.RePicLink(text):
                item=EhentaiPageItem()
                item['pagenumber']=response.url.split('/')[6].split('?')[0].split('-')[1]
                item['booknumber']=response.url.split('/')[6].split('?')[0].split('-')[0]
                item['url']=url
                yield item
