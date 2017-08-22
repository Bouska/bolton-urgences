import scrapy

class CHCPSpider(scrapy.Spider):
    name = "chpc"
    start_urls = ['http://www.ch-cotentin.fr/usager/ecran-delais-urgence']

    def parse(self, response):
        yield {
            'pAttente' : int(response.xpath('//div[@class="row"][3]/div[2]/text()').re_first(r'\d{1,}')),
            'pTraitement' : int(response.xpath('//div[@class="row"][2]/div[2]/text()').re_first(r'\d{1,}'))
        }
