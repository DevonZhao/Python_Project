import scrapy
from DiseaseSpider.items import DiseasespiderItem


class DiseaseSpider(scrapy.Spider):
    i = 0
    name = "disease"
    allowed_domains = ["http://www.familydoctor.com.cn/"]
    start_urls = [
        "http://jbk.familydoctor.com.cn/position.html"
    ]

    for i in range(188):
        url_head = "http://jbk.familydoctor.com.cn/position_0_0_%d.html" % (i)
        start_urls.append(url_head)
    print(start_urls)
    # def parse(self, response):
    #     filename = response.url.split("/")[-2]+'.txt'
    #     response
    #     print(filename)
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)




    def parse(self, response):
        for sel in response.xpath('//div[@class="ill-lists"]/ul/li[not(@class="empty")]'):    # 排除某个子节点使用not语法，具体见https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/not
            # print(sel) # 在调试的时候可以打印出sel的内容便于分析
            item = DiseasespiderItem()
            item['symptom_name'] = sel.xpath('a/text()').extract()
            item['symptom_link'] = sel.xpath('a/@href').extract()
            item['disease_name'] = sel.xpath('p/i/text()').extract()
            yield item


