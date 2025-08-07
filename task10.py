treasure = {
    "clues": ["beach", "cave", "waterfall"],
    "locations": {
        "beach": {
            "items": ["compass", "shovel"],
            "hint": "dig here"
        },
        "cave": {
            "items": ["compass", "shovel"],
            "hint": "dig here"
        }
    },
    "crew": ["First Mate", "Navigator"]
}
treasure["crew"].append("Cook")
treasure["locations"]["volcano"] = {
"items": ["diamond", "lava boots"],
"hint": "wear protection"
}
treasure["clues"].append("volcano")
treasure["crew"].remove("Navigator")
for location in treasure["locations"]:
    items = treasure["locations"][location]["items"]
    for i in items:
        if i == "gold coin":
            print(f"Treasure found in {location}")
    print(f"{location} : {', '.join(items)}")