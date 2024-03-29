# Información equipo

## Integrantes

- Daniel Erazo
- Santiago Rassa

# Vista Funcional del sistema implementado
![entrega_final_d_c_c](https://github.com/danierazome/propiedades-alpes-rassa-2024/assets/124007154/fcabbac4-f523-446c-b20a-053054003286)


## Vista de Despliegue
![image](https://github.com/danierazome/propiedades-alpes-rassa-2024/assets/124007154/cf8f1e30-8cd2-4db3-abf4-25c3e4797b25)
# Instrucciones correr conponentes local

## Requisitos

- Docker
- Postman o similar
- Recomendable ejucutar el servicio en ambiente UNIX ya sea Linux o MacOS

## Pasos Despliegue local

- Clonar este repositorio en ambiente local en la rama Main
- Ir a la raíz del repositorio en el ambiente local
- Ejecutar -> docker compose up
- Realizar pruebas utilizando la collection que se encuetra adjunta

## Pasos Despliegue Kluster K8s
- Clear instancia de base de datos en su provedor de nube
- Crear cluster de K8s en su provedor de nube
- Despliegue Pulsar siguiendo [esta documentación](https://pulsar.apache.org/docs/next/getting-started-helm/)
- Actualice el archivo secrets.yaml presente en la raiz del proyecto agregando la ip de Pulsar y datos de conexión a la base de datos
- Ejecute en su cluster el siguiente comando para guardar en un vault los secretos: kubectl apply -f secrets.yaml
- Ejecute en su cluster el siguiente comando para crear los deployments y servicios para sus componentes: kubectl apply -f k8s-services.yaml
- Ejecute en su cluster el siguiente comando para configurar las reglas de autoscaling: kubectl apply -f autoscaling.yaml
- Ejecute en su cluster el siguiente comando para crear el Ingress para su aplicación: kubectl apply -f ingress.yaml
- Revise la salud de sus pods. Estos seran desplegados en el namespace default: kubectl get pods
- Para revisar con mas detalle los logs de sus pods: kubectl logs <pod_name>


## Collection
[Colección de Postman](https://github.com/danierazome/propiedades-alpes-rassa-2024/files/14569593/NO-MONOLITerazICAS.postman_collection.json)


## Video
[Video-Entrega](https://github.com/danierazome/propiedades-alpes-rassa-2024/wiki/Entrega-5#video-entrega)

# Entrega final

## Video
[Video entrega final](https://drive.google.com/file/d/1hcoGl1X8Fi9-47BeYz1q0YokXsqvn5Sh/view)

## Documentación
[Wiki](https://github.com/danierazome/propiedades-alpes-rassa-2024/wiki/Entrega-5)
