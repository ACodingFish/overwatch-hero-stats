# https://overwatch.blizzard.com/en-us/rates/?input=PC&map=all-maps&region=Americas&role=All&rq=2&tier=Silver

import requests
from overwatch_hero_stats.logger import Logger
from .hero_filters import HeroFilters, HFType

TEST_MODE = False

if TEST_MODE:
    from .fake_data import fake_data

class HeroDataFetcher:
    def __init__(self):
        self.URL = "https://overwatch.blizzard.com/en-us/rates/data/"
        self.logger = Logger()
        self.generic_data = self.fetch_data(HeroFilters())

    def _assemble_URL(self, herofilters: HeroFilters) -> str:
        url = self.URL
        # herofilters here
        url += herofilters.export_params()
        return url

    def fetch_data(self, herofilters: HeroFilters) -> dict:
        hero_dict :dict = {}

        url = self._assemble_URL(herofilters)
        # self.logger.debug(f"Fetching from URL:{url}")

        if TEST_MODE:
            self.logger.debug("Fake Data")
            hero_dict : dict = fake_data
        else:
            #Don't cause a load on servers
            from time import sleep
            from random import randint
            sleep_sec = randint(1,3)
            sleep(sleep_sec)
        
            try:
                r = requests.get(url)
            except Exception as e:
                self.logger.error(f"Invalid URL:{e}")
                return hero_dict
            try:
                hero_dict : dict = r.json()
            except Exception as e:
                self.logger.error(f"Response was not JSON:{e}")


        # Role filter doesn't do anything on API side, handle locally
        role = herofilters.filters[HFType.ROLE.value].value_name()
        if (role.lower() != "all"):
            role_heroes = self.get_hero_dict_by_role(role).keys()
            rate_data : dict = hero_dict.get("rates", {})
            rate_list : list = rate_data.get("rates", [])
            new_rate_list : list = [rate for rate in rate_list if rate.get("id","") in role_heroes]
            rate_data["rates"] = new_rate_list
            hero_dict["rates"] = rate_data
        return hero_dict
    
    def get_hero_dict(self) -> dict:
        hero_dict : dict = {}

        rate_data : dict = self.generic_data.get("rates", {})
        rate_list : list = rate_data.get("rates", [])
        
        for hero_rate in rate_list:
            hero_id = hero_rate.get("id", None)
            if (hero_id):
                hero_data = hero_rate.get("hero", {})
                hero_data.pop("portrait", "")
                hero_data.pop("roleIcon", "")
                hero_dict[hero_id] = hero_data
        # self.logger.debug(hero_dict)

        return hero_dict
    
    def get_hero_dict_by_role(self, role: str = "All"):
        hero_dict : dict = self.get_hero_dict()
        role_filter = role.lower()
        if (role_filter == "all"):
            return hero_dict
        
        filtered_hero_dict = {}
        for hero_id, hero_data in hero_dict.items():
            hero_role = hero_data.get("role", "").lower()
            hero_subrole = hero_data.get("subrole", "").lower()
            if (role_filter == hero_role) or (role_filter == hero_subrole):
                filtered_hero_dict[hero_id] = hero_data
        return filtered_hero_dict
    
    def get_winrate_for_hero(self, hero_id : str = "anran", rate_list: list = []):
        winrate = {}
        for rate in rate_list:
            if rate.get("id", "unknown") == hero_id:
                winrate = rate.get("cells", {})
                break
        return winrate

    
    def get_winrates_for_heroes(self, hero_ids: dict[str]=["anran", "genji", "soldier-76"], data: dict = {}):
        if data == {}:
            data = self.generic_data

        hero_dict = self.get_hero_dict()

        rate_data : dict = data.get("rates", {})
        rate_list : list = rate_data.get("rates", [])

        hero_winrates = {}
        for hero_id in hero_ids:
            if hero_id not in hero_dict:
                self.logger.warn(f"Could not find hero with id: {hero_id}")
                continue
            winrate: dict = self.get_winrate_for_hero(hero_id, rate_list)
            hero_winrates[hero_id] = winrate
        return hero_winrates
            
    def get_best_hero(self, hero_ids: dict[str]=["anran", "genji", "soldier-76"], data: dict = {}, count = 1):
        hero_winrates = self.get_winrates_for_heroes(hero_ids=hero_ids, data=data)
        hero_queue : list = []
        for hero_id in hero_ids:
            hero_data = hero_winrates.get(hero_id, {})

            winrate = hero_data.get("winrate", 0)
            if not winrate:
                continue

            pickrate = hero_data.get("pickrate", 0)
            if not pickrate:
                continue

            idx = 0
            for hero in hero_queue:
                queued_winrate = hero[1].get("winrate", 0)
                queued_pickrate = hero[1].get("pickrate", 0)
                if queued_winrate > winrate:
                    idx+=1
                elif (queued_winrate == winrate) and (queued_pickrate < pickrate):
                    idx+=1
                else:
                    break

            hero_queue.insert(idx, (hero_id, hero_data))
            

            if len(hero_queue) > count:
                hero_queue.pop()
            
        return hero_queue
    
    # Find sleepers - >50% winrate, but low usage < 5%
            
            


