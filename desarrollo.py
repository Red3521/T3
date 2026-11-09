import math
import random

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))


if a <= 0 or b <= 0 or c <= 0 or d <= 0:
  print("Error: Todos los parámetros deben ser mayores a cero.")
  exit()

puntos_elipse = 0
puntos_interseccion = 0

for _ in range(cantidad):
  x = random.uniform(-a, a)
  y = random.uniform(-b, b)

  if (x**2) / (a**2) + (y**2) / (b**2) <= 1:
    puntos_elipse += 1

    if (x**2) / (c**2) - (y**2) / (d**2) >= 1:
      puntos_interseccion += 1

area_elipse_formula = math.pi * a * b

if puntos_elipse > 0:
  area_interseccion_montecarlo = (
      puntos_interseccion / puntos_elipse
  ) * area_elipse_formula
else:
  area_interseccion_montecarlo = 0


print("\n========== RESULTADOS ==========")
print(f"Puntos aleatorios que cayeron dentro de la elipse: {puntos_elipse}")
print(f"Puntos aleatorios que cayeron en la intersección de la hipérbola con la elipse:"f" {puntos_interseccion}")
print(f"\nÁrea de la elipse por fórmula: {area_elipse_formula:.6f}")
print(f"Área aproximada de la zona de intersección por Monte Carlo:"f" {area_interseccion_montecarlo:.6f}")