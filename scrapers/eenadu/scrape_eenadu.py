import scrapy
from scrapy.crawler import CrawlerProcess

scraped_urls = []
all_titles = []

class EenaduSpider(scrapy.Spider):
    name = 'telugu-news'
    start_urls = ['https://www.eenadu.net/']

    def parse(self, response):
        for title in response.css('.article-title'):
            if title.css('::text').get():
                all_titles.append(title.css('::text').get())
                yield {"title: " + title.css('::text').get()}

        if response.css('a'):
            for next_page in response.css('a'):
                if next_page.css('a').attrib['href'].startswith("https://www.eenadu.net"):
                    yield response.follow(next_page, self.parse)
        else:
            scraped_urls.append(response.css('a').attrib['href'])


def scrapycrawl():
    process = CrawlerProcess()
    process.crawl(EenaduSpider)
    process.start()


# main function
if __name__ == "__main__":
    # website to be scraped
    site = "https://www.eenadu.net"

    # calling function
    # scrape(site)
    scrapycrawl()

    print(all_titles)
    print(scraped_urls)
