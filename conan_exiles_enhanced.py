from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MyOptions:
    pass

class MyGame(Game):
    name = "Conan Exiles Enhanced"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
    ]

    is_adult_only_or_unrated = False
    options_cls = MyOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(

                label="Build (or add to a town) a CRAFTING_BUILDING in the River Biome",
                data={
                    "CRAFTING_BUILDING": (self.crafting_building, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=25,
            ),
            GameObjectiveTemplate(

                label="Build (or add to a town) a SOCIAL_BUILDING in the River Biome",
                data={
                    "SOCIAL_BUILDING": (self.social_building, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=25,
            ),
            GameObjectiveTemplate(

                label="Build (or add to a town) a MILITARY_BUILDING in the River Biome",
                data={
                    "MILITARY_BUILDING": (self.military_building, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=15,
            ),
            GameObjectiveTemplate(

                label="Clear the RIVER_CAVE in the River Biome",
                data={
                    "RIVER_CAVE": (self.river_cave, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=10,
            ),
            GameObjectiveTemplate(

                label="Clear RIVER_CAMP in the River Biome",
                data={
                    "RIVER_CAMP": (self.river_camp, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=15,
            ),
            GameObjectiveTemplate(

                label="Rescue PRISONER from thrall cage in the River Biome.",
                data={
                    "PRISONER": (self.prisoner, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=15,
            ),
            GameObjectiveTemplate(

                label="Capture THRALL and drag im to a Well of Pain in the River Biome.",
                data={
                    "THRALL": (self.thrall, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=15,
            ),
            GameObjectiveTemplate(

                label="Gather RIVER_RESOURCE in the River Biome.",
                data={
                    "RIVER_RESOURCE": (self.river_resource, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=15,
            ),
        ]
        
    crafting_building = [
        "Blacksmith",
        "Armorer",
        "Lumber Mill",
        "Tannery",
        "Weaver / Tailor",
        "Mine",
        "Artisan Workshop", 
    ]
    social_building = [
        "House",
        "Tavern",
        "Inn",
        "Fisherman's Hut",
        "Stable",
        "Treasure Room",
        "Market Stall",
        "Merchant House"
        "Slaves Market"
        "Shrines"
    ]
    military_building = [
        "Barracks",
        "Watchtower",
        "Training Yard",
        "Archery Range",
        "Prison / Jail",
        "Town Gate",
        "Rampart",
        "Fortified Keep",
    ]
    river_cave = [
        "Hanuman's Grotto cave",
        "Sinner's Refuge cave",
        "Dregs dungeon",
    ]
    river_camp = [
        "an Exile camp",
        "the Lookout Point camp",
        "the Marrowman's Height camp",
        "the Narrowneck Span camp",
        "the Riverwatch Camp",
        "the Scavenger's Berth camp",
        "the Skulker's End camp",
    ]
    prisoner = [
        "1 prisoner",
        "2 prisoners",
        "3 prisoners",
    ]
    thrall = [
        "Alchemist",
        "Archer",
        "Armorer",
        "Bearer",
        "Blacksmith",
        "Carpenter",
        "Cook",
        "Fighter",
        "Performer",
        "Priest",
        "Smelter",
        "Tanner",
        "Taskmaster",
    ]
    river_resource = [
        "100 x Crystal",
        "100 x Iron ore",
        "250 x Stone",
        "250 x Wood Log",
        "100 x Branch",
        "100 x Hide",
        "50 x Aloe Leaves",
        "100 x Plant Fiber",
        "10 x Mushroom",
        "10 x Yellow Lotus",
        "10 x Orange Phykos",
        "10 x Glowing Goop",
    ]
