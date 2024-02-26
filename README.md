[NO-MONOLITICAS.postman_collection.json](https://github.com/danierazome/propiedades-alpes-rassa-2024/files/14411286/NO-MONOLITICAS.postman_collection.json)# Información equipo

## Integrantes

- Daniel Erazo
- Santiago Rassa

# Servicio Listado propiedades
## Vista Informacion
![apps_no_monoliticas-FUNCIONAL_MODULO_PROPIEDADES](https://github.com/danierazome/propiedades-alpes-rassa-2024/assets/124007154/9d8d706f-55f1-4bb6-b359-1a4c63ef4dc7)

# Instrucciones correr conponentes

## Requisitos

- Docker
- Postman o similar
- Recomendable ejucutar el servicio en ambiente Linux

## Pasos

- Clonar este repositorio en ambiente local en la rama Main
- Ir a la raíz del repositorio en el ambiente local
- Ejecutar -> docker compose up
- Realizar pruebas utilizando la collection que se encuetra adjunta

## Collection
[Upload{
	"info": {
		"_postman_id": "a25f8819-1d42-490f-8676-289a334deaaa",
		"name": "NO-MONOLITICAS",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "28920849"
	},
	"item": [
		{
			"name": "CREAR_CARACTERIZACION",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"propiedad_id\": \"312-3232-3232-32\",\n    \"floors\": 10,\n    \"zone\": 2,\n    \"type\": \"INDUSTRIAL\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:5000/caracterizacion",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5000",
					"path": [
						"caracterizacion"
					]
				}
			},
			"response": []
		},
		{
			"name": "OBTENER_CARACTERIZACION",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:5000/caracterizacion/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5000",
					"path": [
						"caracterizacion",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "OBTENER_DISPONIBILIDADES",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:5000/disponibilidad/",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "5000",
					"path": [
						"disponibilidad",
						""
					]
				}
			},
			"response": []
		}
	]
}ing NO-MONOLITICAS.postman_collection.json…]()


