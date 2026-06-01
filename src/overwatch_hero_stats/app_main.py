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
from .data_fetcher.hero_options.hero_role import HeroRole
# END


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
        herofilters.update_filters()
        fetcher = HeroDataFetcher()
        
        # full_roster = fetcher.get_hero_dict().keys()
        role ="damage"
        role_roster = fetcher.get_hero_dict_by_role(role)

        for map in HeroMap.__members__:
            herofilters.update_filters(map=HeroMap[map].value, role=HeroRole[role].value, tier=HeroTier.Silver.value,)
            hero_data = fetcher.fetch_data(herofilters)
            best_heroes = fetcher.get_best_hero(hero_ids=role_roster, data=hero_data, count=2)
            logger.debug(f"Best Heroes ({map}): {best_heroes}")