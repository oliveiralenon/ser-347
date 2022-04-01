from math import radians, cos, sin, asin, sqrt

r = 6371

print('-------Calculadora de distância entre duas coordenadas-------\n')
print('Primeira coordenada')
lat1 = radians(float(input('Digite a latitude em graus decimais: ')))
long1 = radians(float(input('Digite a longitude em graus decimais: ')))

print('Segunda coordenada')
lat2 = radians(float(input('Digite a latitude em graus decimais: ')))
long2 = radians(float(input('Digite a longitude em graus decimais: ')))

distancia =  (2 * r) * (asin(sqrt(((sin((lat2 - lat1) / 2)) ** 2) + ((cos(lat1)) * (cos(lat2)) * (sin((long2 - long1)/2) ** 2)))))

print(f"A distância entre as coordenadas é {distancia} km")