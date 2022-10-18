import random
from playwright.sync_api import sync_playwright
from PageToSunroofDtoTranslator import PageToSunroofDtoTranslator
import time


class Scraper:
    def scrapeByLatLongs(self, latLongs):
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'
        ]
        user_agent = random.choice(user_agents)

        result = []
        # i = 0
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(extra_http_headers={'User-Agent': user_agent})

            translator = PageToSunroofDtoTranslator()
            # start_time = time.time()

            for latLong in latLongs:
                context = browser.new_context(record_video_dir="videos/") 
                page.goto(
                    "https://sunroof.withgoogle.com/building/" + str(latLong[0]) + "/" + str(-1*latLong[1]) + "/#?f=buy")
                context.close()
                result.append(translator.translate(page, latLong))
            # if len(latLongs)>0:
            #     print("--- %s seconds per address ---" % ((time.time() - start_time) / len(latLongs)))
            browser.close()
        return result
