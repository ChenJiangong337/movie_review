# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewItem(Item):
    User_ID = Field()
    date = Field()
    score = Field()
    approve = Field()
    short_review = Field()
    movie_name = Field()
    pass
class MovieIDItem(Item):
    movie_ID = Field()
    pass
