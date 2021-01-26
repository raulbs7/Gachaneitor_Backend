# Gachaneitor Backend

Este repositorio contiene el software necesario para el despliegue de una página web, cuya función será la de proporcionar un entorno en el que se podrán subir recetas de la famosa Gachaneitor. Esto se hará mediante el envío de recetas en el lenguaje propio de este dominio.

## Pre-requisitos 📋

Antes de ejecutar el servidor por el cual se desplegará esta página web, se deben instalar una serie de requisitos.

El primer requisito es instalar la versión de Python 3.8.
Para instalar las dependencias es recomendable crear un entorno virtual con el módulo de entornos virtuales ``venv``.

Este módulo permite aislar las dependencias entre distintos proyectos, creando diferentes intérpretes para cada uno con sus respectivas dependencias. El siguiente comando crea un intérprete en el directorio elegido.

```
python3 -m venv venv
```

Si se escoge crear un entorno virtual, la forma de utilizar el intérprete es usando el siguiente comando:

```
source venv/bin/activate
```

Para volver a usar el intérprete por defecto del sistema se tiene que ejecutar el siguiente comando:

```
deactivate
```

Tanto si se hace la instalación de las dependencias en un entorno virtual, como si se hace en el intérprete por defecto del sistema, los requisitos del proyecto se instalan utilizando el siguiente comando.

```
pip3 install -r requirements.txt
```

## Despliegue 📦

Para ejecutar el servidor y para que la web pueda ser consultada, debemos iniciar el servidor de Django. Para ello se debe entrar en la carpeta *gachaneitor* y ejecutar el siguiente comando:

```
python3 manage.py runserver
```

Una vez que se ha iniciado el server, para entrar a la web debemos de escribir la siguiente dirección en el navegador: __http://127.0.0.1:8000__

## Herramientas

Como se ha mencionado en la documentación, las herramientas utilizadas para crear esta web han sido las siguiente

* [Django](https://docs.djangoproject.com/en/3.1/) - Documentación de Django.
* [ANTLR](https://www.antlr.org/)
* Javascript, CSS y plantillas HTML.


## Autores

* **Raúl Bernalte Sánchez** [raulbs7](https://github.com/raulbs7)
* **Enrique Cepeda Villamayor** [EnriqueCepeda](https://github.com/EnriqueCepeda)
* **Elena Hervás Martín** [elenahrvs](https://github.com/elenahrvs)
* **Elena María Ruíz Izquierdo** [elenamariaruiz](https://github.com/elenamariaruiz)
