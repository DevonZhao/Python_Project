import scrapy
from DiseaseSpider.items import DiseasespiderItem
from scrapy.http import Request

from scrapy.spider import Spider
from scrapy.selector import Selector


class DiseaseSpider(scrapy.Spider):
    i = 0
    name = "disease"
    allowed_domains = ["http://www.familydoctor.com.cn/"]
    start_urls = [
        "http://jbk.familydoctor.com.cn/position.html"
    ]

    # 188
    for i in range(2):
        url_head = "http://jbk.familydoctor.com.cn/position_0_0_%d.html" % (i)
        start_urls.append(url_head)
    print(start_urls)

    # 直接写文件
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)



    # 爬取首页的信息，不包括跳转的页面。
    # def parse(self, response):
    #     for sel in response.xpath('//div[@class="ill-lists"]/ul/li[not(@class="empty")]'):    # 排除某个子节点使用not语法，具体见https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/not
    #         # print(sel) # 在调试的时候可以打印出sel的内容便于分析
    #         item = DiseasespiderItem()
    #         item['symptom_name'] = sel.xpath('a/text()').extract()
    #         item['symptom_link'] = sel.xpath('a/@href').extract()
    #         item['disease_name'] = sel.xpath('p/i/text()').extract()
    #         yield item

    def parse(self, response):
        contents = response.xpath('//div[@class="ill-lists"]/ul/li[not(@class="empty")]')
        for sel in contents:
            item = DiseasespiderItem()
            item['symptom_name'] = sel.xpath('a/text()').extract()
            item['disease_name'] = sel.xpath('p/i/text()').extract()
            item['symptom_link'] = str(sel.xpath('a/@href').extract())
            next_url = str(sel.xpath('a/@href').extract())
            print("url的数据类型：" + next_url)
            yield Request(url=next_url, meta={'item': item}, callback=self.parse_disease_detail)

    def parse_disease_detail(self,response):
        item = response.meta['item']
        # sel = Selector(response)
        # item['disease_desc'] = response.xpath('//div[@class="ill-why-com il-info"]/p/text()').extract()
        # print(response.xpath('//div[@class="ill-why-com il-info"]/p/text()').extract())
        yield item








