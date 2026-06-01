# Test

from .logger import Logger
from .data_fetcher.hero_fetcher import HeroDataFetcher, HeroOptions

class main_app:
    def start():
        logger = Logger()
        logger.setHTTPLogLevel()
        logger.info("Fetching hero data...")
        options = HeroOptions()
        fetcher = HeroDataFetcher()
        fetcher.fetch_data(options)