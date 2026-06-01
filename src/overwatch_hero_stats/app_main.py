# Test

from .logger import Logger
from .data_fetcher.hero_fetcher import HeroDataFetcher
from .data_fetcher.hero_filters import HeroFilters, HFType

#TEST
from .data_fetcher.hero_options.hero_map import HeroMap
from .data_fetcher.hero_options.hero_tier import HeroTier
from .data_fetcher.hero_options.hero_input import HeroInput
from .data_fetcher.hero_options.hero_queue_type import HeroQueueType
from .data_fetcher.hero_options.hero_region import HeroRegion
# END


def test_filters(herofilters: HeroFilters, map: HeroMap = HeroMap.circuit_royal.value):
    herofilters.set_filter_value(HFType.INPUT, HeroInput.PC.value)
    herofilters.set_filter_value(HFType.MAP, map)
    herofilters.set_filter_value(HFType.TIER, HeroTier.Silver.value)
    herofilters.set_filter_value(HFType.QUEUE_TYPE, HeroQueueType.COMP_Role_Queue.value)
    herofilters.set_filter_value(HFType.REGION, HeroRegion.Americas.value)

current_roster = [
            "soldier-76",
            "genji",
            "anran",
            "sojourn"
        ]

class main_app:
    def start():
        logger = Logger()
        logger.setHTTPLogLevel()
        logger.info("Fetching hero data...")
        herofilters = HeroFilters()
        test_filters(herofilters)
        fetcher = HeroDataFetcher()
        # hero_dict = fetcher.get_hero_dict()

        for map in HeroMap.__members__:
            test_filters(herofilters, HeroMap[map].value)
            hero_data = fetcher.fetch_data(herofilters)
            best_heroes = fetcher.get_best_hero(hero_ids=current_roster, data=hero_data, count=3)
            logger.debug(f"Best Heroes ({map}): {best_heroes}")