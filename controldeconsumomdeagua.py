
def calcular_objetivo_ml(peso_kg, nivel_actividad):
    objetivo = peso_kg * 35

    if nivel_actividad == "bajo":
        objetivo *= 0.9
    elif nivel_actividad == "alto":
        objetivo *= 1.1

    return objetivo


def estado_hidratacion(consumo_ml, objetivo_ml):
    if consumo_ml < objetivo_ml:
        porcentaje = ((objetivo_ml - consumo_ml) / objetivo_ml) * 100
        return f"Te falta un {porcentaje:.2f}% para llegar"
    
    elif consumo_ml == objetivo_ml:
        return "Has alcanzado tu objetivo"
    
    else:
        porcentaje = ((consumo_ml - objetivo_ml) / objetivo_ml) * 100
        return f"Has excedido tu objetivo en un {porcentaje:.2f}%"


personas = []

while True:
    try:
        print("\n--- Nueva persona ---")
        
        peso = float(input("Ingrese su peso en kg: "))
        
        nivel = input("Ingrese nivel de actividad (bajo, medio, alto): ").lower()
        if nivel not in ["bajo", "medio", "alto"]:
            print("Nivel de actividad inválido")
            continue
        
        consumo = float(input("Ingrese agua consumida en ml: "))
        
    
        objetivo = calcular_objetivo_ml(peso, nivel)
        estado = estado_hidratacion(consumo, objetivo)
        
        
        persona = {
            "peso": peso,
            "actividad": nivel,
            "consumo": consumo,
            "objetivo": objetivo
        }
        
        personas.append(persona)
        
    
        print(f"Objetivo diario: {objetivo:.2f} ml")
        print(estado)
    
    except ValueError:
        print("Error: ingresaste un dato inválido")
    
    
    seguir = input("¿Desea cargar otra persona? (s/n): ").lower()
    if seguir != "s":
        break

print("\n--- Resumen de personas ---")

for i, p in enumerate(personas, start=1):
    print(f"\nPersona {i}:")
    print(f"Peso: {p['peso']} kg")
    print(f"Actividad: {p['actividad']}")
    print(f"Consumo: {p['consumo']} ml")
    print(f"Objetivo: {p['objetivo']:.2f} ml")