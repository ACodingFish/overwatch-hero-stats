
from .hero_options.filter_enum import FilterEnum

from .hero_options.hero_input import HeroInput
from .hero_options.hero_map import HeroMap
from .hero_options.hero_region import HeroRegion
from .hero_options.hero_role import HeroRole
from .hero_options.hero_queue_type import HeroQueueType
from .hero_options.hero_tier import HeroTier

class HeroFilters:
    def __init__(self):  
        self.input : HeroInput = HeroInput.default()
        self.map : HeroMap = HeroMap.default()
        self.region : HeroRegion = HeroRegion.default()
        self.role : HeroRole = HeroRole.default()
        self.queue_type : HeroQueueType = HeroQueueType.default()
        self.tier : HeroTier = HeroTier.default()

    def export_params(self):
        filters : list[FilterEnum] = []
        filters.append(self.input)
        filters.append(self.map)
        filters.append(self.region)
        filters.append(self.role)
        filters.append(self.queue_type)
        filters.append(self.tier)

        param_list = []
        for filter in filters:
            if filter is not None:
                param_list.append("=".join([filter.filter_name(), filter.value_param()]))

        return "?" + "&".join(param_list)