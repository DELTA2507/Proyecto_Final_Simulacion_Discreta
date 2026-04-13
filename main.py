from drones import create_drone
from simulation import generate_orders, assign_orders, move_drones, update_deliveries
from utils import print_state


def run_simulation():
    state = {
        "drones": [create_drone("D1"), create_drone("D2"), create_drone("D3")],
        "orders": []
    }

    total_steps = 5

    for t in range(total_steps):
        generate_orders(state, t)
        assign_orders(state)
        move_drones(state)
        update_deliveries(state)

        print_state(t, state, total_steps)


run_simulation()