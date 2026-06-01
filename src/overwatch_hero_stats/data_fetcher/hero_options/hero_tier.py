from .filter_enum import FilterEnum

class HeroTier(FilterEnum):
    def __init__(self):
        self.filter_str = "tier"

    All=()
    Bronze=()
    Silver=()
    Gold=()
    Platinum=()
    Diamond=()
    Master=()
    Grandmaster=()