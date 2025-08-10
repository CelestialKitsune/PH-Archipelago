from enum import IntEnum

class EntranceGroups(IntEnum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    # Areas
    HOUSE = 1 << 3
    CAVE = 2 << 3
    ISLAND = 3 << 3
    OVERWORLD = 4 << 3
    DUNGEON_ENTRANCE = 5 << 3
    BOSS = 6 << 3
    DUNGEON_ROOM = 7 << 3
    WARP_PORTAL = 8 << 3
    # Bitmasks
    DIRECTION_MASK = HOUSE - 1
    AREA_MASK = ~0 << 3


OPPOSITE_ENTRANCE_GROUPS = {
    EntranceGroups.RIGHT: EntranceGroups.LEFT,
    EntranceGroups.LEFT: EntranceGroups.RIGHT,
    EntranceGroups.UP: EntranceGroups.DOWN,
    EntranceGroups.DOWN: EntranceGroups.UP
}

ENTRANCE_DATA = {
    # "Name <self> -> <exit>": {
    #   "entrance": tuple[int, int, int], stage room entrance.
    #   "region": str. logic region that the entrance is in
    #   "exit": int scene id. Scene it leads -> in vanilla
    #   "region_return": str. if the entrance is logically one way, the region you exit ->.
    #   "two_way": bool. generates a reciprocal entrance if the logic requirements are loose
    # }

    "Mercay SW -> Oshus": {
        "entrance": (0xB, 0, 2),
        "exit": (0xB, 0xA, 1),
        "entrance_region": "mercay sw",
        "exit_region": "mercay oshus",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "two_way": True
    },
    "Mercay SW -> Apricot": {
        "entrance": (0xB, 0x0, 3),
        "exit": (0xB, 0xB, 1),
        "entrance_region": "mercay sw",
        "exit_region": "mercay apricot",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "two_way": True
    },
    "Mercay SW -> Sword Cave": {
        "entrance": (0xB, 0x0, 4),
        "exit": (0xB, 0x13, 1),
        "entrance_region": "mercay sw",
        "exit_region": "mercay sword cave",
        "type": EntranceGroups.CAVE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SW -> Mercay NW": {
        "entrance": (0xB, 0x0, 0xFC),
        "exit": (0xB, 0x1, 0xFB),
        "entrance_region": "mercay sw",
        "exit_region": "mercay nw",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.UP,
    },
    "Mercay SW -> Mercay SE": {
        "entrance": (0xB, 0x0, 0xFD),
        "exit": (0xB, 0x3, 0xFE),
        "entrance_region": "mercay sw bridge",
        "exit_region": "mercay nw",
        "type": EntranceGroups.OVERWORLD,
        "direction": EntranceGroups.RIGHT,
    },
    "Mercay SE -> Milk Bar": {
        "entrance": (0xB, 0x3, 0x3),
        "exit": (0xB, 0xC, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay milk bar",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE -> Shipyard": {
        "entrance": (0xB, 0x3, 0x4),
        "exit": (0xB, 0xD, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay shipyard",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE -> Tuzi": {
        "entrance": (0xB, 0x3, 0x5),
        "exit": (0xB, 0xE, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay tuzi",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE -> Treasure Teller": {
        "entrance": (0xB, 0x3, 0x6),
        "exit": (0xB, 0xF, 0x0),
        "entrance_region": "mercay se",
        "exit_region": "mercay treasure teller",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
    },
    "Mercay SE -> Mercay Shop": {
        "entrance": (0xB, 0x3, 0xFC),
        "exit": (0xB, 0x11, 0xFB),
        "entrance_region": "mercay se",
        "exit_region": "mercay shop",
        "type": EntranceGroups.HOUSE,
        "direction": EntranceGroups.UP,
        "two_way": True
    },

    # "Mercay SE -> Mercay NE": {
    #     "entrance": (0xB, 0x3, 0x7),
    #     "exit": (0xB, 0x11, 0x1),
    #     "two_way": True
    # },
    # "Mercay NE -> Freedle Tunnel": {
    #     "entrance": (0xB, 0x2, 0x2),
    #     "exit": (0xB, 0x12, 0x3),
    #     "two_way": True
    # },
    # "Freedle Island -> Freedle Tunnel": {
    #     "entrance": (0xB, 0x2, 0x3),
    #     "exit": (0xB, 0x12, 0x2),
    #     "two_way": True
    # },
    # "Mercay NE -> Mercay NE": {
    #     "entrance": (0xB, 0x3, 0x7),
    #     "exit": (0xB, 0x11, 0x1),
    #     "two_way": True
    # },


}

OPPOSITES = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

ENTRANCES = {}
i = 0
for name, data in ENTRANCE_DATA.items():
    ENTRANCES[name] = data
    ENTRANCES[name]["id"] = i
    print(f"{i} {ENTRANCES[name]['entrance_region']} -> {ENTRANCES[name]['exit_region']}")
    i += 1

    if data.get("two_way", True):
        name_list = name.split(" -> ")
        reverse_name = name_list[1] + " -> " + name_list[0]
        reverse_data = {
            "entrance_region": data.get("reverse_exit_region", data["exit_region"]),
            "exit_region": data.get("reverse_entrance_region", data["entrance_region"]),
            "id": i,
            "entrance": data["exit"],
            "exit": data["entrance"],
            "two_way": True,
            "type": data["type"],
            "direction": OPPOSITE_ENTRANCE_GROUPS[data["direction"]]
        }
        ENTRANCES[reverse_name] = reverse_data
        print(f"{i} {ENTRANCES[reverse_name]['entrance_region']} -> {ENTRANCES[reverse_name]['exit_region']}")
        i += 1






if __name__ == "__main__":
    for name, data in ENTRANCES.items():
        print(f"{name}:", "{")
        for k, v in data.items():
            print(f"\t{k}: {v}")
        print("},")
