# # # Task10 Ex.1
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
# # ////////////////////////////////////////////////////////////////////
# # # Task10 Ex.2
brackets = input("Brackets: ")
items = brackets.split()
for item in items:
    stack = []
    balanced = True
    for item in items:
        if item == "(" or item == "{" or item == "[":
            stack.append(item)
        elif item == ")" or item == "}" or item == "]":
            if not stack:
                balanced = False
                break
            last = item[-1]
        if item == ")" and last != "(" or item == "]" and last != "[" or item == "}" and last != "{":
            balanced = False
            break
        if balanced and not stack:
            print(f"{item} Balanced")
        else:
            print(f"{item} Imbalanced") 
# ////////////////////////////////////////////////////////////////////
# # Task10 Ex.3
import heapq
customers = ["Alex", "Bob", "Sarah", "Maria", "Mike"]
vips = ["Alex", "Maria"]
vip_queue = []
regular_queue = []
for customer in customers:
    if customer in vips:
        vip_queue.append(customer)
    else:
        regular_queue.append(customer)
serve = vip_queue + regular_queue
print(serve)