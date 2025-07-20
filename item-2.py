from math import radians, cos, sin, asin, sqrt

# Ciudades con coordenadas
ciudades_chile = {
    "Santiago": (-33.4489, -70.6693),
    "Valparaíso": (-33.0458, -71.6197),
    "Concepción": (-36.8201, -73.0444),
    "La Serena": (-29.9023, -71.2519),
    "Temuco": (-38.7359, -72.5904),
    "Antofagasta": (-23.6509, -70.3975)
}

ciudades_argentina = {
    "Buenos Aires": (-34.6118, -58.3960),
    "Córdoba": (-31.4201, -64.1888),
    "Rosario": (-32.9442, -60.6505),
    "Mendoza": (-32.8908, -68.8272),
    "La Plata": (-34.9215, -57.9545),
    "Tucumán": (-26.8083, -65.2176)
}

transportes = {
    "1": {"nombre": "Automóvil", "velocidad": 80},
    "2": {"nombre": "Autobús", "velocidad": 60},
    "3": {"nombre": "Avión", "velocidad": 500},
    "4": {"nombre": "Bicicleta", "velocidad": 20},
    "5": {"nombre": "Caminando", "velocidad": 5}
}

def calcular_distancia(coord1, coord2):
    """Calcula distancia usando fórmula de Haversine"""
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    
    return c * 6371  # Radio de la Tierra en km

def formatear_tiempo(horas):
    """Convierte horas a formato legible"""
    if horas > 24:
        dias = int(horas // 24)
        horas_restantes = int(horas % 24)
        return f"{dias}d {horas_restantes}h"
    else:
        h = int(horas)
        m = int((horas - h) * 60)
        return f"{h}h {m}m"

def mostrar_ciudades(ciudades, pais):
    """Muestra lista de ciudades"""
    print(f"\n--- Ciudades de {pais} ---")
    for i, ciudad in enumerate(ciudades.keys(), 1):
        print(f"{i}. {ciudad}")

def seleccionar_ciudad(ciudades, tipo):
    """Selecciona una ciudad"""
    while True:
        try:
            opcion = int(input(f"\nSeleccione ciudad de {tipo} (número): "))
            if 1 <= opcion <= len(ciudades):
                ciudad = list(ciudades.keys())[opcion - 1]
                return ciudad, ciudades[ciudad]
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")

def seleccionar_transporte():
    """Selecciona medio de transporte"""
    print("\n--- Medios de Transporte ---")
    for key, info in transportes.items():
        print(f"{key}. {info['nombre']}")
    
    while True:
        opcion = input("\nSeleccione transporte (número): ")
        if opcion in transportes:
            return transportes[opcion]
        else:
            print("Opción inválida.")

def main():
    print("="*40)
    print("  CALCULADORA DISTANCIAS CHILE-ARGENTINA")
    print("="*40)
    
    while True:
        try:
            # Seleccionar origen (Chile)
            print("\n=== CIUDAD DE ORIGEN (Chile) ===")
            mostrar_ciudades(ciudades_chile, "Chile")
            origen, coord_origen = seleccionar_ciudad(ciudades_chile, "origen")
            
            # Seleccionar destino (Argentina)
            print("\n=== CIUDAD DE DESTINO (Argentina) ===")
            mostrar_ciudades(ciudades_argentina, "Argentina")
            destino, coord_destino = seleccionar_ciudad(ciudades_argentina, "destino")
            
            # Seleccionar transporte
            transporte = seleccionar_transporte()
            
            # Calcular distancia y tiempo
            distancia_km = calcular_distancia(coord_origen, coord_destino)
            distancia_millas = distancia_km * 0.621371
            tiempo_horas = distancia_km / transporte['velocidad']
            
            # Mostrar resultado
            print("\n" + "="*40)
            print("           RESULTADO DEL VIAJE")
            print("="*40)
            print(f"Origen: {origen} (Chile)")
            print(f"Destino: {destino} (Argentina)")
            print(f"Transporte: {transporte['nombre']}")
            print("-"*40)
            print(f"Distancia: {distancia_km:.0f} km ({distancia_millas:.0f} millas)")
            print(f"Tiempo estimado: {formatear_tiempo(tiempo_horas)}")
            print("-"*40)
            print("NARRATIVA DEL VIAJE:")
            print(f"1. Salida desde {origen}")
            print(f"2. Viaje en {transporte['nombre'].lower()}")
            print("3. Cruce de frontera Chile-Argentina")
            print(f"4. Llegada a {destino}")
            print("="*40)
            
            # Preguntar si continuar
            while True:
                continuar = input("\n¿Continuar? (Enter) o 's' para salir: ").lower()
                if continuar == 's':
                    print("\n¡Hasta luego! 👋")
                    return
                elif continuar == '':
                    break
                else:
                    print("Presione Enter para continuar o 's' para salir.")
                    
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego! 👋")
            return
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()