# Test

from .logger import Logger
from .data_fetcher.hero_fetcher import HeroDataFetcher
from .data_fetcher.hero_filters import HeroFilters, HFType

#TEST
from .data_fetcher.hero_options.hero_input import HeroInput
from .data_fetcher.hero_options.hero_map import HeroMap
from .data_fetcher.hero_options.hero_tier import HeroTier
from .data_fetcher.hero_options.hero_queue_type import HeroQueueType
from .data_fetcher.hero_options.hero_region import HeroRegion
# END


def test_filters(herofilters: HeroFilters,
        input: int = HeroInput.PC.value,
        map: int = HeroMap.all_maps.value,
        tier: int = HeroTier.All.value,
        queue_type = HeroQueueType.COMP_Role_Queue.value,
        region = HeroRegion.Americas.value,
    ):
    herofilters.set_filter_value(HFType.INPUT, input)
    herofilters.set_filter_value(HFType.MAP, map)
    herofilters.set_filter_value(HFType.TIER, tier)
    herofilters.set_filter_value(HFType.QUEUE_TYPE, queue_type)
    herofilters.set_filter_value(HFType.REGION, region)

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
        
        full_roster = fetcher.get_hero_dict().keys()

        for map in HeroMap.__members__:
            test_filters(herofilters=herofilters, tier=HeroTier.Silver.value, map=HeroMap[map].value)
            hero_data = fetcher.fetch_data(herofilters)
            best_heroes = fetcher.get_best_hero(hero_ids=full_roster, data=hero_data, count=1)
            logger.debug(f"Best Heroes ({map}): {best_heroes}")