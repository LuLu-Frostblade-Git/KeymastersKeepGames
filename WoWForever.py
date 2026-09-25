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
    name = "World of Warcraft Forever"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
    ]

    is_adult_only_or_unrated = False
    options_cls = MyOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(

                label="Gain LEVEL levels as a member of the FACTION",
                data={
                    "LEVEL": (self.level, 1),
                    "FACTION": (self.faction, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            
            GameObjectiveTemplate(

                label="Gain LEVEL levels as a WOW_CLASS",
                data={
                    "LEVEL": (self.level, 1),
                    "WOW_CLASS": (self.wow_class, 1),
                },

                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            
            GameObjectiveTemplate(

                label="Gain SKILL_POINT skill point in PROFESSION",
                data={
                    "SKILL_POINT": (self.skill_point, 1),
                    "PROFESSION": (self.profession, 1),
                },

                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            
            GameObjectiveTemplate(

                label="Gather STACK stacks of RESSOURCE",
                data={
                    "STACK": (self.stack, 1),
                    "RESSOURCE": (self.ressource, 1),
                },

                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            
            GameObjectiveTemplate(

                label="Complete QUEST quests on CHARACTER",
                data={
                    "QUEST": (self.quest, 1),
                    "CHARACTER": (self.character, 1),
                },

                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            
            GameObjectiveTemplate(

                label="Complete DUNGEON on CHARACTER",
                data={
                    "DUNGEON": (self.dungeon, 1),
                    "CHARACTER": (self.character, 1),
                },

                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
        ]

    faction = [
        "Alliance",
        "Horde",
    ]

    level = [
        "2",
        "3",
        "4",
        "5",
    ]
    
    wow_class = [
        "Druid",
        "Hunter",
        "Mage",
        "Paladin",
        "Priest",
        "Rogue",
        "Shaman",
        "Warlock",
        "Warrior",
    ]
    
    skill_point = [
        "10",
        "15",
        "20",
        "25",
    ]

    profession = [
        "Blacksmithing",
        "Leatherworking",
        "Engineering",
        "Enchanting",
        "Tailoring",
        "Alchemy",
        "Cooking",
        "Mining",
        "Fishing",
        "Skinning",
        "Herbalism",
        "First Aid",
        "Alchemy",
        "Tailoring",
        "Enchanting",
        "any profession",
    ]
    
    stack = [
        "2",
        "3",
        "4",
        "5",
    ]
    
    ressource = [
        "Ores",
        "Herbs",
        "Skins",
        "Fishs",
        "Cloths",
        "Meats",
    ]
    
    quest = [
        "10",
        "15",
        "20",
        "25",
    ]
    
    character = [
        "any character",
        "an horde character",
        "an alliance character",
    ]
    
    dungeon = [
        "1 dungeon",
        "2 dungeons",
        "3 dungeons",
    ]
