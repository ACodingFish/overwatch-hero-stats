# Test

from .logger import Logger
from .data_fetcher.hero_fetcher import HeroDataFetcher, HeroFilters

class main_app:
    def start():
        logger = Logger()
        logger.setHTTPLogLevel()
        logger.info("Fetching hero data...")
        herofilters = HeroFilters()
        fetcher = HeroDataFetcher()
        # fetcher.fetch_data(herofilters)
        fetcher.get_hero_dict()