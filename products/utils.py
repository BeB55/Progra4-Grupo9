import requests
from django.conf import settings
from decimal import Decimal

def calcular_ruta(lat_origen, lng_origen, lat_destino, lng_destino):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        "Authorization": settings.ORS_API_KEY,
        "Content-Type": "application/json",
    }
    body = {
        "coordinates": [
            [lng_origen, lat_origen],
            [lng_destino, lat_destino],
        ]
    }

    try:
        r = requests.post(url, json=body, headers=headers)
        r.raise_for_status()
        data = r.json()

        # ✅ Adaptado al nuevo formato de respuesta
        route = data["routes"][0]
        segment = route["segments"][0]

        distance_m = segment["distance"]
        duration_s = segment["duration"]

        return {
            "distance_km": round(distance_m / 1000, 2),
            "duration_min": round(duration_s / 60, 2),
            "geometry": route["geometry"],
        }

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al llamar a ORS: {e}")
        return None
    except (KeyError, IndexError) as e:
        print("⚠️ Estructura inesperada en la respuesta de ORS:", e)
        return None


def calcular_costo_delivery(distance_km, base_cost=Decimal('200.00'), cost_per_km=Decimal('50.00')):
    """Calcula el costo total del envío."""
    if distance_km <= 0:
        return base_cost
    return base_cost + (Decimal(distance_km) * cost_per_km)

