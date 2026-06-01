from .filter_enum import FilterEnum, merge_enums


class AllRoles(FilterEnum):
    All=()

class DamageRoles(FilterEnum):
    damage=()
    flanker=()
    sharpshooter=()
    specialist=()
    recon=()

class SupportRoles(FilterEnum):
    support=()
    medic=()
    tactician=()
    survivor=()

class TankRoles(FilterEnum):
    tank=()
    stalwart=()
    initiator=()
    bruiser=()

__ALL_ROLES__ = [
    AllRoles,
    DamageRoles,
    SupportRoles,
    TankRoles,
]

HeroRole = merge_enums("role", "HeroRole", __ALL_ROLES__)