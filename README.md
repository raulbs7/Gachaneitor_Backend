# Gachaneitor Backend

_Este repositorio contiene el software necesario para el despliegue de una página
web, cuya función será la de proporcionar un entorno en el que se podrán subir
recetas de la famosa Gachaneitor. Esto se hará mediante el envió de recetas en el
lenguaje propio de este dominio._

## Pre-requisitos 📋

Antes de ejecutar el servidor por el cual se desplegará esta página web, deberán de
instalarse una serie de requisitos.

Para ello, es recomendable crear un entorno virtual con 
el módulo de entornos virtuales ``venv``.
```
python3 -m venv venv
```

Una vez elegido si la instalación sea en entorno virtual o en el propio entorno de
Python, se debe instalar los requisitos del archivo ``requirements.txt``.
```
pip install -r requirements.txt
```

## Despliegue 📦

Para ejecutar el servidor, y que la web pueda ser consultada, debemos iniciar Django. 
Para ello se debe ejecutar el siguiente comando.
```
python3 manage.py runserver
```

Una vez que se ha iniciado el server, para entrar a la web debemos de escribir la siguiente
dirección en el navegador: __http://127.0.0.1:8000__

## Herramientas

Como ya se ha mencionado, la herramienta utilizada para crear esta web será 

* [Django](https://docs.djangoproject.com/en/3.1/) - Documentación de Django.

## Autores

* **Raúl Bernalte Sánchez** [raulbs7](https://github.com/raulbs7)
* **Enrique Cepeda Villamayor** [EnriqueCepeda](https://github.com/EnriqueCepeda)
* **Elena Hervás Martín** [elenahrvs](https://github.com/elenahrvs)
* **Elena María Ruíz Izquierdo** [elenamariaruiz](https://github.com/elenamariaruiz)
