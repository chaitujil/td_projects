import scrapy
import csv

from scrapy.crawler import CrawlerProcess

scraped_urls = []
all_titles = []

header = ['title', 'text', 'link']

f = open('eenadu_data.csv', 'w', encoding='UTF8')
writer = csv.writer(f)
writer.writerow(["title", "text", "link"])


class EenaduSpider(scrapy.Spider):
    name = 'telugu-news-bot1'
    start_urls = ['https://www.eenadu.net']

    def parse(self, response):
        current_link = response.url
        last_token = current_link.split("/")[-1]
        if last_token.isdigit() and \
                "photos" not in current_link and "video" not in current_link:
            if current_link.startswith("https://www.eenadu.net/"):
                # print("Scraped: " + current_link)
                scraped_urls.append(current_link)
                title = response.xpath("//h1[@class='red']/text()").extract()
                text = response.css(".fullstory").xpath(".//p//text()").getall()
                filtered_titles = [x for x in title if not x.isalpha()]
                filtered_text = [x for x in text if not x.isalpha()]
                full_title = ' '.join(filtered_titles)
                full_text = ' '.join(filtered_text)
                if full_title and full_text:
                    all_titles.append(full_title)
                    writer.writerow([full_title, full_text, current_link])
                    yield {'title': full_title, 'text': full_text}

        if response.css('a') and not last_token.isdigit():
            for next_page in response.css('a'):
                next_page_link = next_page.css('a').attrib['href']
                if next_page_link.startswith("https://www.eenadu.net/"):
                    if next_page_link not in scraped_urls:
                        scraped_urls.append(next_page_link)
                        yield response.follow(next_page, self.parse)
        else:
            scraped_urls.append(response.css('a').attrib['href'])
            yield None


class EenaduSpider2(scrapy.Spider):
    name = 'telugu-news-bot2'
    start_urls = ['https://www.eenadu.net/']

    def parse(self, response):
        current_link = response.url
        last_token = current_link.split("/")[-1]
        if last_token.isdigit() and \
                "photos" not in current_link and "video" not in current_link:
            if current_link.startswith("https://www.eenadu.net/"):
                # print("Scraped: " + current_link)
                scraped_urls.append(current_link)
                title = response.xpath("//h1[@class='red']/text()").extract()
                text = response.css(".fullstory").xpath(".//p//text()").getall()
                filtered_titles = [x for x in title if not x.isalpha()]
                filtered_text = [x for x in text if not x.isalpha()]
                full_title = ' '.join(filtered_titles)
                full_text = ' '.join(filtered_text)
                if full_title and full_text:
                    all_titles.append(full_title)
                    writer.writerow([full_title, full_text, current_link])
                    yield {'title': full_title, 'text': full_text}

        if response.css('a') and not last_token.isdigit():
            for next_page in response.css('a'):
                next_page_link = next_page.css('a').attrib['href']
                if next_page_link.startswith("https://www.eenadu.net/"):
                    if next_page_link not in scraped_urls:
                        scraped_urls.append(next_page_link)
                        yield response.follow(next_page, self.parse)
        else:
            scraped_urls.append(response.css('a').attrib['href'])
            yield None


# main function
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(EenaduSpider)
    process.crawl(EenaduSpider2)
    process.start()

    print(all_titles)
    print(scraped_urls)
    f.close()
