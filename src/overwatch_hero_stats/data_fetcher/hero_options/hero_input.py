from .filter_enum import FilterEnum

class HeroInput(FilterEnum):
    def __init__(self):
        self.filter_str = "input"

    PC=()
    Console=()
