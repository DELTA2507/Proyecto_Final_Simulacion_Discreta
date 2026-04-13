import random
from graph import graph


def generate_orders(state, t):
    if t % random.randint(2, 4) == 0:
        targets = ["P1", "P2", "P3", "P4", "P5"]
        dest = random.choice(targets)

        state["orders"].append({
            "id": f"O{t}-{random.randint(100,999)}",
            "destination": dest,
            "status": "pending"
        })


def assign_orders(state):
    for order in state["orders"]:
        if order["status"] != "pending":
            continue

        available = [d for d in state["drones"] if d["state"] == "available"]
        if not available:
            return

        drone = random.choice(available)

        drone["order"] = order
        drone["state"] = "busy"
        order["status"] = "assigned"


def move_drones(state):
    for drone in state["drones"]:
        if drone["state"] != "busy" or not drone["order"]:
            continue

        if not drone["path"]:
            drone["path"] = find_path(drone["position"], drone["order"]["destination"])

        if not drone["path"]:
            continue

        next_node = drone["path"].pop(0)

        for edge in graph[drone["position"]]:
            if edge[0] == next_node:
                _, _, battery_cost, _, _ = edge

                drone["battery"] -= battery_cost + random.randint(-1, 2)
                drone["position"] = next_node

                break


def update_deliveries(state):
    for drone in state["drones"]:
        if drone["state"] == "busy" and drone["order"]:
            if drone["position"] == drone["order"]["destination"]:
                drone["order"]["status"] = "delivered"
                drone["order"] = None
                drone["state"] = "available"
                drone["path"] = []


def find_path(start, end):
    queue = [(start, [start])]
    paths = []

    while queue:
        node, path = queue.pop(0)

        if node == end:
            paths.append(path[1:])
            continue

        for edge in graph.get(node, []):
            neighbor = edge[0]
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    if not paths:
        return []

    return random.choice(paths)