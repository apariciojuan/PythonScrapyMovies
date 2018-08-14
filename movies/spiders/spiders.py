import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from movies.items import MoviesItem

class MovieSpyder(CrawlSpider):
    name = 'movie'
    item_count = 0 #controla la cantidad de item a procesar no el spyder
    allowed_domain = ['miradetodo.io/']
    start_urls = ['http://miradetodo.io/?s=']
#    start_urls = ['http://miradetodo.io/category/animacion/']
    rules = {
		# rules looking for next page and save individual item to callback
     Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@class="nav-previous alignleft"]/a'))),
	 Rule(LinkExtractor(allow =(), restrict_xpaths = ('//*[@class="item"]/a')),
							callback = 'parse_item', follow = False)
	         }

    def parse_item(self, response):
        movie_item = MoviesItem()
        #normalize-space es para sacar los espacios en blancos que sobran
        movie_item['name'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/h1)').extract()
        movie_item['description'] = response.xpath('normalize-space(//*[@id="cap1"]/p[1])').extract()
        movie_item['year'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[1]/span[2]/a)').extract()
        movie_item['times'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[1]/span[3]/i)').extract()
        movie_item['category'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[1]/i)').extract()
        movie_item['year_start'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/span/i[2])').extract()
        movie_item['director'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[2])').extract()
        movie_item['actors'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[3])').extract()
        movie_item['country'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[5])').extract()
        movie_item['clasified_year'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/p[1]/span[1])').extract()
        movie_item['original_title'] = response.xpath('normalize-space(//*[@id="uwee"]/div[2]/span/i[1])').extract()
        movie_item['image_urls'] = response.xpath('normalize-space(//*[@id="uwee"]/div[1]/div/img/@src)').extract()
        movie_item['image_name'] = response.xpath('normalize-space(//*[@id="uwee"]/div[1]/div/img/@alt)').extract()
        movie_item['linkType'] = response.xpath("normalize-space(//div[@class='player_nav']/ul[@class='idTabs']/li[2]/a)").extract()
        movie_item['linkRepos'] = response.xpath("normalize-space(//*[@id='div2']/div/iframe/@src)").extract()
        for x in range(3, 6): #looking for more version of the movie
            path = "normalize-space(//div[@class='player_nav']/ul[@class='idTabs']/li[%s]/a)" % str(x)
            path1 = "normalize-space(//*[@id='div%s']/div/iframe/@src)" % str(x)
            data = response.xpath(path).extract()[0]
            data1 = response.xpath(path1).extract()[0]
            if (data != '') and (data1 != ''): #if there are more save it
                movie_item['linkType'].append(data)
                movie_item['linkRepos'].append(data1)
            else:
                break
        self.item_count += 1
        if self.item_count > 4: #limit to item processed
            raise CloseSpider('item_exceeded')
        yield movie_item
