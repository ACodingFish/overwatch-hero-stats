# https://overwatch.blizzard.com/en-us/rates/?input=PC&map=all-maps&region=Americas&role=All&rq=2&tier=Silver

import requests
from overwatch_hero_stats.logger import Logger
from .hero_filters import HeroFilters


class HeroDataFetcher:
    def __init__(self):
        self.URL = "https://overwatch.blizzard.com/en-us/rates/data/"
        self.logger = Logger()

    def assembleURL(self, herofilters: HeroFilters) -> str:
        url = self.URL
        # herofilters here
        url += herofilters.export_params()
        return url

    def fetch_data(self, herofilters: HeroFilters) -> dict:
        hero_dict :dict = {}

        url = self.assembleURL(herofilters)
        self.logger.debug(f"Fetching from URL:{url}")
        try:
            pass #r = requests.get(url)
        except Exception as e:
            self.logger.error(f"Invalid URL:{e}")
            return hero_dict
        try:
            pass #hero_dict = r.json()
            # print(hero_dict)
        except Exception as e:
            print(f"Response was not JSON:{e}")
        return hero_dict

