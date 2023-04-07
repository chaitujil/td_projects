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
                yield {'title': title.css('::text').get()}

        if response.css('a'):
            for next_page in response.css('a'):
                next_page_link = next_page.css('a').attrib['href']
                if next_page_link.startswith("https://www.eenadu.net"):
                    if next_page_link not in scraped_urls:
                        yield response.follow(next_page, self.parse)
        else:
            scraped_urls.append(response.css('a').attrib['href'])
            yield None


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
