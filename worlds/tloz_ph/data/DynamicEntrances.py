from .Entrances import ENTRANCES

def create_scene_id(entrance):
    e_stage, e_room, e_entrance = entrance
    return e_stage * 0x100 + e_room

DYNAMIC_ENTRANCES = {
    "Shortcut to TotOK": {
        "entrance": "Mercay SE Tuzi",
        "destination": "TotOK Lobby Exit"
    }
}

DYNAMIC_ENTRANCES_BY_SCENE = {}
print("assigning dynamic entrances")
for name, data in DYNAMIC_ENTRANCES.items():
    data["name"] = name
    entrance_data = ENTRANCES[data["entrance"]]
    destination_data = ENTRANCES[data["destination"]]

    entrance_scene = create_scene_id(entrance_data["entrance"])
    detect_scene = create_scene_id(entrance_data["exit"])

    link_coords = entrance_data.get("coords", None)

    # Handle extra data
    extra_data = {"y": link_coords[1]} if link_coords else {}  # Ensure that the y value is always checked
    extra_data |= entrance_data.get("extra_data", {})  # Contains additional boundaries and stuff
    extra_data = tuple(extra_data.items()) if extra_data else None
    coords = list(link_coords) if link_coords else [None]

    # Values for Client.er_in_scene
    exit_data = list(destination_data["entrance"]) + coords
    detect_data = tuple(list(entrance_data["exit"]) + [extra_data])


    print(f"\tscene: {entrance_scene}")
    print(f"\t\t{detect_data} => {exit_data}")

    # Save er_in_scene values in data
    data["detect_data"] = detect_data
    data["exit_data"] = exit_data

    DYNAMIC_ENTRANCES_BY_SCENE.setdefault(entrance_scene, dict())
    DYNAMIC_ENTRANCES_BY_SCENE[entrance_scene][name] = data
