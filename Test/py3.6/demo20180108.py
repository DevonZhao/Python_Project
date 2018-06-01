

start_urls = [
    "http://jbk.familydoctor.com.cn/position.html"
]
i = 0
for i in range(187):
    url_head = "http://jbk.familydoctor.com.cn/position_0_0_%d.html" % (i)
    start_urls.append(url_head)
print(start_urls)

