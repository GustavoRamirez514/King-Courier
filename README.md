# KingCourier

![logo](https://i.ibb.co/yP1YJG8/Leon-500x500.png)


Aplicación web para una empresa de mensajería que permita gestionar y hacer seguimiento a los paquetes que envían sus clientes. La aplicación debe permitir gestionar la información de clientes, mensajeros y permitir la operación de envío y entrega de paquetes. Debe tener un módulo de administración que le permita al gerente de la empresa sacar reportes en formato PDF con la información de los pedidos solicitados por cliente y por mes, y de pedidos atendidos por mensajero en un mes especificado.

# Índice

- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Pruebas](#pruebas)
- [Despliegue](#despliegue)
- [Monitoreo de la Aplicación](#monitoreo-de-la-aplicación)
- [Organización del Proyecto](#organización-del-proyecto)


## Requisitos

- Python
- Django
- Bootstrap
- HTML
- CSS
- JavaScript

## Configuración del Entorno

1. Clonamos el repositorio desde GitHub:
```
git clone https://github.com/miche890/King-Courier.git
```

2. Instalamos las dependencias del proyecto:
``` python
pip install -r requirements.txt
```

3. Configuramos las variables de entorno necesarias para la aplicación, como las credenciales de la base de datos.

4. Realizamos cualquier otra configuración específica que pueda ser necesaria para nuestro proyecto, como las secrets en nuestro respositorio de GitHub.

## Ejecución del Proyecto

1. Aplicamos las migraciones:
``` python
python manage.py migrate
```

2. Ejecutamos el servidor de desarrollo de Django:

``` python
python manage.py runserver
```
Esto iniciará el servidor de desarrollo y podrás acceder a la aplicación en http://localhost:8000.

## Pruebas

Las pruebas de la aplicacion se realizan automaticamente con GitActions.

- Las pruebas unitarias se ejecutan automáticamente cuando se hace un commit o un pull request a la rama develop. Los resultados de las pruebas se pueden ver en la sección de acciones en el repositorio de GitHub.

- Las pruebas de SonarCloud también se activan cuando se realiza un commit o un pull request en la rama develop. Los resultados y métricas de calidad del código se pueden ver en la interfaz de SonarCloud.

## Despliegue

El despliegue de la aplicación se realiza automáticamente en Render.com.

1. Nos aseguramos de que el repositorio de GitHub esté conectado a Render.com y configurado correctamente.

2. Realizamos los cambios necesarios en nuestro código y realizamos un commit en la rama main.

3. Render.com detectará automáticamente el nuevo commit y generará un nuevo evento de despliegue.

4. Una vez que el despliegue se haya completado, podremos acceder a la aplicación en la URL proporcionada por Render.com.

## Monitoreo de la Aplicación

1. Configuramos las integraciones de Slack para recibir notificaciones de eventos relevantes, como commits, creación de imágenes de Docker, escaneos de SonarCloud, modificaciones en Trello, etc. Encontramos esta información sobre cómo configurar las notificaciones en Slack en la documentación de Slack y en las herramientas específicas que estamos utilizando para la integración.

## Organización del Proyecto

Menciona que estás utilizando Trello para la organización del proyecto en colaboración con tu compañera de trabajo. Puedes mencionar cómo se utilizan las tarjetas, listas y tableros en Trello para gestionar las tareas y el progreso del proyecto.
