# Test

from .logger import Logger
from .data_fetcher.hero_fetcher import HeroDataFetcher
from .data_fetcher.hero_filters import HeroFilters, HFType

class main_app:
    def start():
        logger = Logger()
        logger.setHTTPLogLevel()
        logger.info("Fetching hero data...")
        herofilters = HeroFilters()
        herofilters.set_filter_value(HFType.MAP, 3)
        fetcher = HeroDataFetcher()
        fetcher.fetch_data(herofilters)
        fetcher.get_hero_dict()