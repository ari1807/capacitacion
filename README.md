# Contenido

Este repositorio contiene las resoluciones a distintas las distintas actividades propuestas por la capacitación. Cada carpeta refiere a una actividad distinta:

- **seven-display**: resolución a la actividad propuesta para utilizar TDD hecha en el lenguaje Python, junto con un archivo test.py realizado con la herramienta [unittest](https://docs.python.org/3/library/unittest.html). El módulo display.py contiene la función convert_number, que recibe un número por parámetro y lo convierte en un string de números mostrados en display de la forma:
```
    _  _  _ 
  ||_|  ||_|
  | _|  ||_|
```
- **actividad-vagrant**: contiene un archivo [Vagrant](https://www.vagrantup.com) que crea y ejecuta una MV Ubuntu 18.07 y la aprovisiona utilizando el archivo bootstrap.sh. Entre las aplicaciones que instala el script se encuentra el servidor web Apache, que permite mostrar en el puerto 8080 de localhost un Currículum creado con [JSON resume](https://jsonresume.org)
- **ansible-vagrant**: contiene un archivo Vagrant que crea y ejecuta una MV Ubuntu 18.07 y la aprovisiona utilizando ansible. Algunas de las configuraciones de este archivo fueron declaradas para que pueda funcionar en WSL, utilizando como herramienta de virtualización VirtualBox. Entre las aplicaciones que instala el script se encuentra el servidor web Apache, que permite mostrar en el puerto 8080 de localhost un Currículum creado con JSON resume.