# https://overwatch.blizzard.com/en-us/rates/?input=PC&map=all-maps&region=Americas&role=All&rq=2&tier=Silver

import requests
from overwatch_hero_stats.logger import Logger
from .hero_filters import HeroFilters

TEST_MODE = True

if TEST_MODE:
    from .fake_data import fake_data

class HeroDataFetcher:
    def __init__(self):
        self.URL = "https://overwatch.blizzard.com/en-us/rates/data/"
        self.logger = Logger()
        self.generic_data = self.fetch_data(HeroFilters())

    def _assemble_URL(self, herofilters: HeroFilters) -> str:
        url = self.URL
        # herofilters here
        url += herofilters.export_params()
        return url

    def fetch_data(self, herofilters: HeroFilters) -> dict:
        hero_dict :dict = {}

        url = self._assemble_URL(herofilters)
        self.logger.debug(f"Fetching from URL:{url}")

        if TEST_MODE:
            self.logger.debug("Fake Data")
            return fake_data
        
        try:
            r = requests.get(url)
        except Exception as e:
            self.logger.error(f"Invalid URL:{e}")
            return hero_dict
        try:
            hero_dict : dict = r.json()
        except Exception as e:
            self.logger.error(f"Response was not JSON:{e}")
        return hero_dict
    
    def get_hero_dict(self) -> dict:
        hero_dict : dict = {}

        rate_data : dict = self.generic_data.get("rates", {})
        rate_list : list = rate_data.get("rates", [])
        
        for hero_rate in rate_list:
            hero_id = hero_rate.get("id", None)
            if (hero_id):
                hero_data = hero_rate.get("hero", {})
                hero_data.pop("portrait", "")
                hero_data.pop("roleIcon", "")
                hero_dict[hero_id] = hero_data
        self.logger.debug(hero_dict)

        return hero_dict
