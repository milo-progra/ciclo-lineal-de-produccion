import json
import pickle

datos = {}
datos['ubicacion'] = []

ubicacion1 = {"type": "Feature", "geometry": { "type": "Point", "coordinates": [289.3263383, -33.4409602]},"properties": {"EMPRESA": "Panaderia FF", "AREA": "Casa Matriz", "Direccion": "Calle 1 Oficina 1 ", "COMUNA": "Santiago Centro"} }

ubicacion2 = {"type": "Feature", "geometry": { "type": "Point", "coordinates": [289.1893511, -33.3549203]},"properties": {"EMPRESA": "Panaderia FF","AREA": "Cocina", "Direccion": "Calle 2 Oficina 2 ", "COMUNA": "Quilicura"}}

ubicacion3 = {"type": "Feature", "geometry": { "type": "Point", "coordinates": [ 289.2523086, -33.5022488]},"properties": {"EMPRESA": "Panaderia FF", "AREA": "Transporte", "Direccion": "Calle 3 Oficina 3 ", "COMUNA": "Cerrillos"}}




datos['ubicacion'].append(ubicacion1)

datos['ubicacion'].append(ubicacion2)

datos['ubicacion'].append(ubicacion3)

print(len(datos['ubicacion'])) #len indica la cantidad de elementos del array


#Escribir los datos en un archivo  json
with open("cicloProduccion/api/ubicacion/ubicacion_json.json", 'w') as f:
    json.dump(datos, f)


