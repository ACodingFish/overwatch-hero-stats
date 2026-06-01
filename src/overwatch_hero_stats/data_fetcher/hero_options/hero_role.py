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
    medic=()
    tactician=()
    survivor=()

class TankRoles(FilterEnum):
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