Paso 1: Preparación

Asegúrate de tener Python 3.11.2 instalado en tu sistema.
Puedes verificarlo ejecutando el comando python --version en tu terminal. 
Si no tienes Python instalado, descárgalo e instálalo desde el sitio web oficial de Python (https://www.python.org/).
Tener instalado MysqlWorkbench u otro programa que nos permita crear un sqlserver MSSQL en nuestro ordenador.

Paso 2: Crear y activar el entorno virtual

-Abre una terminal o símbolo del sistema.
-Navega hasta la ubicación deseada para crear el entorno virtual para el proyecto "pybuys".
-Ejecuta el siguiente comando para crear el entorno virtual:

---------------------------------
python -m venv pybuys_env
---------------------------------

Esto creará un nuevo directorio llamado "pybuys_env" que contendrá el entorno virtual.
-Activa el entorno virtual ejecutando el siguiente comando:

En Windows:

---------------------------------
pybuys_env\Scripts\activate
---------------------------------

En Linux o macOS:

---------------------------------
source pybuys_env/bin/activate
---------------------------------

Después de ejecutar este comando, verás que el prefijo del terminal cambia y muestra el nombre del entorno virtual entre paréntesis, indicando que el entorno virtual está activo.

Paso 3: Clonar el proyecto y navegar al directorio (SALTAR PASO SI YA SE DISPONE DEL PROYECTO)

-Clona el proyecto "pybuys" desde el repositorio correspondiente utilizando Git o descargándolo como un archivo ZIP.

git clone https://github.com/VictorCodificando/PyBuys.git
o
descargar  como zip	

-Descomprime el archivo ZIP (si se descargó como ZIP) y navega a la carpeta "pybuys".

Paso 4: Instalar las dependencias

-Asegúrate de que tu entorno virtual esté activo (verificar que el prefijo del terminal muestre el nombre del entorno virtual entre paréntesis).
-Ejecuta el siguiente comando para instalar las dependencias requeridas:

---------------------------------
pip install -r requirements.txt
---------------------------------

Esto instalará Django, MSSQL y Pillow, junto con otras dependencias necesarias para el proyecto "pybuys".

Paso 5: Configurar la base de datos

-Abre el archivo pybuys/settings.py en un editor de texto.
-Busca la sección DATABASES y actualiza la configuración según tus credenciales y configuración de MSSQL.
-Crear la bdd en nuestro gestor de bdd con el siguiente código en sql:
---------------------------------
CREATE DATABASE pybuys
---------------------------------

Paso 6: Migrar la base de datos (SIEMPRE QUE SE HAGA CAMBIO A LOS MODELOS DE BDD)

-Asegúrate de que tu entorno virtual esté activo.
-Ejecuta el siguiente comando para crear las migraciones:
---------------------------------
python manage.py makemigrations
---------------------------------

-Ejecuta el siguiente comando para aplicar las migraciones y crear las tablas de la base de datos:

---------------------------------
python manage.py migrate
---------------------------------
Paso 7: Recolectar archivos estáticos: (POR CADA MODIFICACION A LOS ARCHIVOS DENTRO DE STATIC)

-Para ejecutar estos arhivos debemos ejecutar este comando:

---------------------------------
python manage.py collectstatic
---------------------------------

Paso 7: Ejecutar el proyecto

-Asegúrate de que tu entorno virtual esté activo.
-Ejecuta el siguiente comando para iniciar el servidor de desarrollo de Django:

---------------------------------
python manage.py runserver
---------------------------------

Esto iniciará el servidor y mostrará una URL local donde podrás acceder a la página principal de pybuys.