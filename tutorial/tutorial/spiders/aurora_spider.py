import scrapy

from tutorial.items import AuroraItem

class AuroraSpider(scrapy.Spider):
    name = "aurora"
    allowed_domains = ["gi.alaska.edu"]
    start_urls = [
        "http://www.gi.alaska.edu/AuroraForecast"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.css('.aurora-forecast .main'):
            item = AuroraItem()
            item['image'] = sel.css('.image img').extract()
            item['intensity'] = sel.css('.level-3l').extract()
            item['level'] = sel.css('.level-3n').extract()
            item['forecast'] = sel.css('p').extract()
            print item['forecast']
            yield item