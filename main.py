from drones import create_drone
from simulation import generate_orders, assign_orders, move_drones, update_deliveries
from utils import print_state


def run_simulation():
    state = {
        # Se inicializan los drones que actuarán en la simulación
        "drones": [create_drone("D1"), create_drone("D2"), create_drone("D3")],

        # Las órdenes comienzan en vacío
        "orders": []
    }

    # Variable que controla la cantidad de pasos que durará la simulación
    total_steps = 5

    # Se ejecuta tantas veces de acuerdo a los pasos
    for t in range(total_steps):
        # Genera las órdenes aleatorias
        generate_orders(state, t)

        # Asigna las órdenes
        assign_orders(state)

        # Mueve los drones en cada paso
        move_drones(state)

        # Actualiza el estado de las entregas
        update_deliveries(state)

        # Imprime la información de los estados del paso actual
        print_state(t, state, total_steps)

run_simulation()