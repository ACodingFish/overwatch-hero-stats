from .filter_enum import FilterEnum

class HeroRegion(FilterEnum):
    def __init__(self):
        self.filter_str = "region"

    Americas=()
    Asia=()
    Europe=()