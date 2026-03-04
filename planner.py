def crear_plan():
    cliente = input("Nombre del cliente: ")
    pais = input("País a visitar: ")
    dias = int(input("Días de estadía: "))

    costo_diario = 120
    fee_agencia = 300

    costo_total = dias * costo_diario + fee_agencia

    plan = {
        "cliente": cliente,
        "pais": pais,
        "dias": dias,
        "costo_diario": costo_diario,
        "fee_agencia": fee_agencia,
        "costo_total": costo_total
    }

    return plan


if __name__ == "__main__":
    plan = crear_plan()
    print("\n🧳 PLAN DE VIAJE")
    for k, v in plan.items():
        print(f"{k}: {v}")