from .hero_options.filter_enum import FilterEnum

from .hero_options.hero_input import HeroInput
from .hero_options.hero_map import HeroMap
from .hero_options.hero_region import HeroRegion
from .hero_options.hero_role import HeroRole
from .hero_options.hero_queue_type import HeroQueueType
from .hero_options.hero_tier import HeroTier

from enum import Enum

class HFType(Enum):
    INPUT=0
    MAP=1
    REGION=2
    ROLE=3
    QUEUE_TYPE=4
    TIER=5
    FILTER_MAX=6


class HeroFilters:
    def __init__(self):
        self.filters : list[FilterEnum] = [
            HeroInput.default(),
            HeroMap.default(),
            HeroRegion.default(),
            HeroRole.default(),
            HeroQueueType.default(),
            HeroTier.default(),
        ]

    def export_params(self):
        param_list = []
        for filter in self.filters:
            if filter is not None:
                param_list.append("=".join([filter.filter_name(), filter.value_param()]))

        return "?" + "&".join(param_list)
    
    def set_filter_value(self, filter:HFType, index: int):
        if (filter.value < HFType.FILTER_MAX.value):
            self.filters[filter.value] = self.filters[filter.value].get_state_at_index(index)