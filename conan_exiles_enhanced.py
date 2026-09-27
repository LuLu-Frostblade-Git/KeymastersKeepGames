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

                weight=5,
            ),
            GameObjectiveTemplate(

                label="Build (or add to a town) a SOCIAL_BUILDING in the BIOME",
                data={
                    "SOCIAL_BUILDING": (self.social_building, 1),
                    "BIOME": (self.biome, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=5,
            ),
            GameObjectiveTemplate(

                label="Build (or add to a town) a MILITARY_BUILDING in the BIOME",
                data={
                    "MILITARY_BUILDING": (self.military_building, 1),
                    "BIOME": (self.biome, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=5,
            ),
            GameObjectiveTemplate(

                label="Clear the CAVE (Cave)",
                data={
                    "CAVE": (self.cave, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=2,
            ),
            GameObjectiveTemplate(

                label="Clear the DUNGEON (Dungeon)",
                data={
                    "DUNGEON": (self.dungeon, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=2,
            ),
            GameObjectiveTemplate(

                label="Clear the VAULT (Siptah Vault)",
                data={
                    "VAULT": (self.vault, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=2,
            ),
            GameObjectiveTemplate(

                label="Activate the LEYSHRINE (Siptah)",
                data={
                    "LEYSHRINE": (self.leyshrine, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=2,
            ),
            GameObjectiveTemplate(

                label="Clear a CAMP",
                data={
                    "CAMP": (self.camp, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=3,
            ),
            GameObjectiveTemplate(

                label="Rescue PRISONER from thrall cage.",
                data={
                    "PRISONER": (self.prisoner, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=5,
            ),
            GameObjectiveTemplate(

                label="Capture a THRALL and drag im to a Well of Pain.",
                data={
                    "THRALL": (self.thrall, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=5,
            ),
            GameObjectiveTemplate(

                label="Gather RESOURCE.",
                data={
                    "RESOURCE": (self.resource, 1),
                },
              
                is_time_consuming=False,
                is_difficult=False,

                weight=5,
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
    biome = [
        "Desert",
        "Highlands",
        "Jungle",
        "Noob River",
        "Savanna",
        "Frozen North",
        "Tundra",
        "Volcano",
        "North Coast (Siptah)",
        "South Coast (Siptah)",
        "East Coast (Siptah)",
        "West Coast (Siptah)",
        "Redwood Forests (Siptah)",
        "Western Valleys & Peaks (Siptah)",
        "Southern Islands (Siptah)",
    ]
    cave = [
        "Bit-Yakin's Seal",
        "Cavern of Fiends",
        "Dragonmouth",
        "Executioners Entrance",
        "Fuming Cave (Siptah)",
        "Gallaman's Tomb",
        "Glowing Cavern (Siptah)",
        "Hanuman's Grotto",
        "Jhil's Roost",
        "Lockstone Cave",
        "Scuttler's Shortcut",
        "Shaleback Hollow",
        "Sinner's Refuge",
        "Skittering Cavern",
        "Barrow King",
        "Crevice",
        "Depths (Siptah)",
        "Floe",
        "High Way",
        "Passage",
        "Scraps",
        "Undergate",
        "Warren of Degenerates",
        "Weaver's Hollow",
        "Xalthar's Refuge",
    ]
    dungeon = [
        "Dregs",
        "Cyclopean Halls",
        "Wine Cellar",
        "Warmaker's Sanctuary",
        "Midnight Grove",
        "Undergate",
        "Black Keep",
        "Well of Skelos",
        "Passage",
        "Palace of the Witch Queen",
        "The Sunken City",
    ]
    vault = [
        "Sanctuary of the Serpent",
        "Harbor of the Drowned",
        "Volary of Jhil",
        "Volary of the Harpy",
        "Demense of the Demon Spiders",
        "Harbor of the Twice Drowned",
        "Asylum of the Outsiders",
        "Accursed Citadel",
        "Refuge of the Gremlins",
        "Refuge of the Goblinoids",
        "Asylum of the Fiends",
        "Den of the Wolfmen",
        "Sanctuary of the Snakemen",
        "Den of the Wolf-brothers",
        "Bastion of the Bat-demons",
    ]
    leyshrine = [
        "Leyshrine of the Birdmen",
        "Leyshrine of the Demon",
        "Leyshrine of the Goblinoid",
        "Leyshrine of the Serpent",
        "Leyshrine of the Fiends",
        "Leyshrine of the Drowned",
    ]
    camp = [
        "Black Hand Camp",
        "Cimmerian Camp",
        "Dafari Camp",
        "Desert Dogs Camp",
        "Exile Camp",
        "Frost Giant Camp",
        "Lemurian Camp",
        "Relic Hunter Camp",
        "Vanir Camp",
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
    resource = [
        "200 x Black Ice ore",
        "500 x Brimstone",
        "500 x Coal",
        "200 x Crystal",
        "200 x Ice",
        "500 x Iron ore",
        "200 x Obsidian ore",
        "100 x Silverstone",
        "100 x Star Metal ore",
        "100 x Goldstone",
        "1000 x Stone",
        "1000 x Wood Log",
        "200 x Driftwood",
        "200 x Branch",
        "100 x Glowing Goop",
        "200 x Gossamer",
        "200 x Resin",
        "50 x Blood",
        "50 x Demon Blood",
        "50 x Bone",
        "200 x Chitin",
        "50 x Feral Flesh",
        "100 x Fur",
        "100 x Hide",
        "50 x Thick Hide",
        "100 x Reptile Hide",
        "50 x Savoury Flesh",
        "5 x Weathered Skull",
        "5 x Blood Crystal",
        "50 x Aloe Leaves",
        "200 x Plant Fibery",
    ]
