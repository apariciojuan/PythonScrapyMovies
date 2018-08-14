# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # Data movies
    name = scrapy.Field()
    description = scrapy.Field()
    year = scrapy.Field()
    times = scrapy.Field()
    category = scrapy.Field()
    year_start = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    country = scrapy.Field()
    clasified_year = scrapy.Field()
    original_title = scrapy.Field()

    #images
    image_urls = scrapy.Field()
    image_name = scrapy.Field()

    #links
    linkType = scrapy.Field()
    linkRepos = scrapy.Field()
