# Filename: MovieIDSpider.py

import scrapy
from scrapy.selector import Selector
from tutorial.items import MovieIDItem
from scrapy import Request
import json

class MovieIDSpider(scrapy.Spider):
    name = "movieid"
    allowed_domains = ["douban.com"]
    headers = {
        'User-Agent':'Mozilla/5.0(Windows NT 6.1;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        }
    def __init__(self):
        self.n = 0
    def start_requests(self):
        url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
        yield Request(url, headers=self.headers)
    def parse(self,response):
        item = MovieIDItem()
        subjects = json.loads(response.body)
        for subject in subjects['subjects']:
            item['movie_ID'] = subject['id']
            yield item
        if self.n<5:
            self.n += 1
            next_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+str(self.n*20)
            yield Request(next_url, headers=self.headers)


        
