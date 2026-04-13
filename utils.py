def print_state(t, state, total_steps):
    print("\n" + "=" * 60)
    print(f"PASO DE SIMULACIÓN: {t + 1} / {total_steps}")
    print("=" * 60)

    print("\n🚁 ESTADO DE LOS DRONES")
    for d in state["drones"]:
        print(f"- Identificador: {d['id']}")
        print(f"  📍 Ubicación: {d['position']}")
        print(f"  🔋 Batería: {d['battery']}%")
        print(f"  📦 Estado: {d['state']}")
        print(f"  🎯 Pedido: {d['order']['id'] if d['order'] else 'ninguno'}")

    print("\n📦 ESTADO DE LOS PEDIDOS")
    for o in state["orders"]:
        print(f"- {o['id']} → {o['destination']} [{o['status']}]")

    print("\n")