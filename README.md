# citas-openshift

Ejemplo de aplicación para desplegarla sobre kubernetes y openshift. Este ejemplo está basado en el artículo [Learn Kubernetes using Red Hat Developer Sandbox for OpenShift](https://developers.redhat.com/developer-sandbox/activities/learn-kubernetes-using-red-hat-developer-sandbox-openshift).

## Despliegue sobre kubernetes

En este ejemplo se van a desplegar 2 microservicios (`citas-backend` y `citas-frontend`) y un servicio de base de datos mariadb. La aplicación funciona de la siguiente manera:

* `citas-backend`: Es una API RESTful que devuelve información sobre citas famosas de distintos autores famosos. La **versión 1** devuelve información de 6 citas que tiene incluidas en el programa. La **versión 2** lee la información de las citas de una base de datos guardada en un servidor mariadb. La aplicación está construida en python 3.9 y ofrece el servicio en el puerto TCP/10000.

    La API RESTfull tiene los siguientes endpoints:

    * URL: `/`
        * MÉTODO: GET  
        * Devuelve la cadena "qotd" para comprobar que el servicio está funcionando.
    * URL: `/version`
        * MÉTODO: GET 
        * Devuelve una cadena con la versión de la aplicación.
    * URL: `/writtenin`
        * MÉTODO: GET
        * Devuelve una cadena con la versión de python con el que se ha programado.
    * URL: `/quotes`
        * MÉTODO: GET
        * Devuelve un JSON con todas las citas.
    * URL: `/quotes/random`
        * MÉTODO: GET
        * Devuelve un JSON con una cita elegida aleatoriamente.
    * URL: `/quotes/{id}`
        * MÉTODO: GET
        * Devuelve un JSON con la cita correspondiente al identificador indicado en la url.
* `citas-frontend`: Es una aplicación python flask que crea una página web dinámica con una cita aleatoria que lee de `citas-backend` para ello conecta al servicio RESTful usando el nombre indicado en la variable de entorno `CITAS_SERVIDOR`.


