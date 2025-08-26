import scrapy
from kaldata.items import KaldataItem


class KaldataSpiderSpider(scrapy.Spider):
    name = "kaldata_spider"
    # allowed_domains = ["www.kaldata.com"]
    # start_urls = ["https://www.kaldata.com"]

    def start_requests(self):
        url = 'https://www.kaldata.com'
        yield scrapy.Request(url, callback=self.parse)

    
    def parse(self, response):
        urls = response.xpath("//ul[@id='menu-td-demo-header-menu-2']//a/@href").getall()
        for url in urls:
            yield response.follow(url, callback=self.articles)


    def articles(self, response):
        links = response.xpath("//div[@class='td_block_inner tdb-block-inner td-fix-index']//h3//a/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.content)


        for i in range(2, 3):
            next_page_part = response.xpath("//a[@aria-label='next-page']/@href").get()
            if next_page_part:
                next_page = f"{next_page_part[0:-1]}{i}"
                yield response.follow(next_page, callback=self.articles)
            else:
                break



    def content(self, response):
        kaldata_item = KaldataItem()
        body = ""
        kaldata_item['title'] = response.xpath("(//h1)[1]/text()").get()
        kaldata_item['pubdate'] = response.xpath("(//time/@datetime)[1]").get()
        kaldata_item['author'] = response.xpath("(//a[@class='tdb-author-name']/text())[1] | //div[@class='td-post-author-name']//a/text()").get()
        for p in response.xpath("//div[@class='vc_column_inner tdi_121  wpb_column vc_column_container tdc-inner-column td-pb-span8'] | //div[@class='td-post-content tagdiv-type']"):
            kaldata_item['body'] = body.join(p.xpath("//p[not(@*)]//text() | //div[@class='vc_column-inner']//p[not(@style='text-align: left;') and not(@class='font-2')]//text()").getall())
        yield kaldata_item