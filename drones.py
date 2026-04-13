def create_drone(drone_id):
    return {
        "id": drone_id,
        "position": "A1",
        "battery": 100,
        "state": "available",
        "order": None,
        "path": [],
        "progress": 0
    }