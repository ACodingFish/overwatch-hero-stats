# https://overwatch.blizzard.com/en-us/rates/?input=PC&map=all-maps&region=Americas&role=All&rq=2&tier=Silver

import requests
from overwatch_hero_stats.logger import Logger


class HeroOptions:
    def __init__(self):
        self.current_params="?input=PC&map=all-maps&region=Americas&role=All&rq=2&tier=Silver"

    def export_params(self):
        return self.current_params


class HeroDataFetcher:
    def __init__(self):
        self.URL = "https://overwatch.blizzard.com/en-us/rates/data/"
        self.logger = Logger()

    def assembleURLFromOptions(self, options: HeroOptions) -> str:
        url = self.URL
        # Options here
        url += options.export_params()
        return url

    def fetch_data(self, options: HeroOptions) -> dict:
        hero_dict :dict = {}

        url = self.assembleURLFromOptions(options)
        self.logger.debug(f"Fetching from URL:{url}")
        try:
            r = requests.get(url)
        except Exception as e:
            self.logger.error(f"Invalid URL:{e}")
            return hero_dict
        try:
            hero_dict = r.json()
            # print(hero_dict)
        except Exception as e:
            print(f"Response was not JSON:{e}")
        return hero_dict

