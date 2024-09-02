import scrapy

class CostsSpider(scrapy.Spider):
    name = "costs"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ['https://worldpopulationreview.com/country-rankings/internet-cost-by-country']

    def parse(self, response):
        for item in response.css('div.mb-5 tbody.z-10'):
            yield{
                'country': item.css('.z-10 .px-2 a[href]::text').getall(),
                'monthlyCost': item.css('td:nth-child(2)::text').getall(),
                'costPerMbps': item.css('td:nth-child(3)::text').getall()
            }