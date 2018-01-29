import scrapy
from DiseaseSpider.items import DiseasespiderItem


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
    # def parse(self, response):
    #     filename = response.url.split("/")[-2]+'.txt'
    #     response
    #     print(filename)
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)


    # # 单独抓去单个url，不包括跳转的url，即不包括子url。
    # def parse(self, response):
    #     for sel in response.xpath('//div[@class="ill-lists"]/ul/li[not(@class="empty")]'):    # 排除某个子节点使用not语法，具体见https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/not
    #         # print(sel) # 在调试的时候可以打印出sel的内容便于分析
    #         item = DiseasespiderItem()
    #         item['symptom_name'] = sel.xpath('a/text()').extract()
    #         item['symptom_link'] = sel.xpath('a/@href').extract()
    #         item['disease_name'] = sel.xpath('p/i/text()').extract()
    #         yield item




    def parse(self, response):
        for sel in response.xpath('//div[@class="ill-lists"]/ul/li[not(@class="empty")]'):  # 排除某个子节点使用not语法，具体见https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/not
            # print(sel) # 在调试的时候可以打印出sel的内容便于分析
            # item['symptom_name'] = sel.xpath('a/text()').extract()
            item = DiseasespiderItem()
            item['symptom_name'] = sel.xpath('a/text()').extract()
            item['symptom_link'] = sel.xpath('a/@href').extract()
            item['disease_name'] = sel.xpath('p/i/text()').extract()
            link = str(sel.xpath('a/@href').extract()).replace('[\'','').replace('\']','')   # 去除字符['']不然下面的url是认不到的。
            print(link,type(link))
            yield scrapy.Request(link, meta={'item': item}, callback=self.parse_details, dont_filter=True)   #这里为什么yield和return返回的结果是不一样的。

    def parse_details(self, response):
        # hao_url = response.url   # 测试返回url
        # print("这是测试"+hao_url)
        # return hao_url
        for sel1 in response.xpath('//div[@class="ill-why-com il-info"]/p'):
            item = response.meta['item']   # 使用response.meta['item']来调用上面返回的结果
            desc = sel1.xpath('normalize-space(text())').extract()    # sel1.xpath('normalize-space(text())')是表示去除空格
            # print(sel1)
            if desc[0]:    # 判断这个字符串是不是空，还可以使用 s.strip()==''
                item['disease_desc'] = desc
                print(type(desc[0]))
                yield item
            else:
                continue








