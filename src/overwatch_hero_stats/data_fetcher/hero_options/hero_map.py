from .filter_enum import FilterEnum, merge_enums


class AllMaps(FilterEnum):
    all_maps=()

class ControlMaps(FilterEnum):
    antarctic_peninsula=()
    busan=()
    ilios=()
    lijiang_tower=()
    nepal=()
    oasis=()
    samoa=()

class EscortMaps(FilterEnum):
    circuit_royal=()
    dorado=()
    havana=()
    junkertown=()
    rialto=()
    route_66=()
    shambali_monastery=()
    watchpoint_gibraltar=()

class FlashpointMaps(FilterEnum):
    aatlis=()
    new_junk_city=()
    suravasa=()

class HybridMaps(FilterEnum):
    blizzard_world=()
    eichenwalde=()
    hollywood=()
    kings_row=()
    midtown=()
    numbani=()
    paraiso=()

class PushMaps(FilterEnum):
    colosseo=()
    esperanca=()
    new_queen_street=()
    runasapi=()

__ALL_MAPS__ = [
    AllMaps,
    ControlMaps,
    EscortMaps,
    FlashpointMaps,
    HybridMaps,
    PushMaps,
]

HeroMap = merge_enums("map", "HeroMap", __ALL_MAPS__)