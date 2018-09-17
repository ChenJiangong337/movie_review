# Filename: DoubanSpider.py

import scrapy
from scrapy.selector import Selector
from tutorial.items import ReviewItem
from scrapy import Request

class ReviewSpider(scrapy.Spider):
    name = "review"
    allowed_domains = ["douban.com"]
    headers = {
        'User-Agent':'Mozilla/5.0(Windows NT 6.1;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        }
    def __init__(self):
        self.n = 0
        self.nn = 0
        self.movie_ID = 0
    def start_requests(self):
        url = "https://movie.douban.com/explore"
        yield Request(url, headers=self.headers,callback=self.parse0)
    def parse0(self,response):
        selector = Selector(response)
        movie_IDs = [
            25882296,
            26654269,
            27172872,
            27012992,
            27006525,
            27621727,
            30201003,
            27093707,
            26588308,
            27064658,
            24773958,
            26842702,
            27040737,
            26654498,
            26416062,
            26787574,
            27200988,
            26997663,
            27113517,
            27172891]           
        if self.n<20:
            self.movie_ID = str(movie_IDs[self.n])
            movie_url = 'https://movie.douban.com/subject/'+self.movie_ID+'/comments?status=P'
            yield Request(movie_url,headers=self.headers,callback=self.parse1)

    def parse1(self,response):
        item = ReviewItem()
        selector = Selector(response)
        reviews = selector.xpath('//div[@class="comment-item"]')
        for review in reviews:
            check = review.xpath('.//span[@class="comment-info"]/span[2]/@class').extract()[0]
            if 'allstar' in check:
                item['movie_name'] = selector.xpath('//div[@id="content"]/h1/text()').extract()[0]
                item['ID'] = review.xpath('.//span[@class="comment-info"]/a/text()').extract()[0]
                item['date'] = review.xpath('.//span[@class="comment-time "]/text()').extract()[0]
                item['score'] = review.xpath('.//span[@class="comment-info"]/span[2]/@class').re(r'(\d+)')[0]
                item['approve'] = review.xpath('.//span[@class="votes"]/text()').extract()[0]
                item['short_review'] = review.xpath('.//span[@class="short"]/text()').extract()[0]
                yield item
        next_url = response.xpath('//div[@class="center"]/a[@class="next"]/@href').extract()
        #如果这里用的是extract()[0]，那么当next按钮不存在的时候会直接报错，起不到检测next是否存在的作用
        if self.nn<10 and next_url:
            self.nn+=1
            next_url = 'https://movie.douban.com/subject/'+self.movie_ID+'/comments'+next_url[0]
            yield Request(next_url, headers=self.headers,callback=self.parse1)
        else:
            self.n+=1
            self.nn = 0
            url = "https://movie.douban.com/explore"
            yield Request(url,headers=self.headers,callback=self.parse0,dont_filter=True)
        
