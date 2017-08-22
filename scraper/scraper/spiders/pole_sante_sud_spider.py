import scrapy

class PoleSanteSudSpider(scrapy.Spider):
    name = "polesantesud"
    start_urls = ['http://www.polesantesud.fr/consultations/poles/urgences']

    def parse(self, response):
        yield {
            'pAttente' : int(response.xpath('//div[@class="pers"]/div/text()').extract_first()),
            'mAttente' : int(response.xpath('//div[@class="atte"]/div/text()').extract_first())
        }
