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

                label="Build (or add to a town) a CRAFTING_BUILDING in the BIOME",
                data={
                    "CRAFTING_BUILDING": (self.crafting_building, 1),
                    "BIOME": (self.biome, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            
    crafting_building = [
        "Blacksmith",
        "Armorer",
        "Lumber Mill",
        "Tannery",
        "Weaver / Tailor",
        "Mason's Workshop",
        "Artisan Workshop", 
    ]

    biome = [
        "Desert",
        "Highlands",
        "Jungle",
        "Noob River",
        "Savanna",
        "Frozen North",
        "Tundra",
        "Volcano",
    ]
