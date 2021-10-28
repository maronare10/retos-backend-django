# Semana 4 Backend - Reto 10

### Paso 1: Instalación del proyecto

Para instalar este proyecto se necesita instalar las librerias que estan en el archivo requirements.txt:

Nota: No olvide configurar la base de datos en MySQL llamada "condominio", para más info ver DATABASES en condominio/settings.py.

```
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
username: admin
email: admin@condominio.com
password: password

python manage.py runserver
```

### Paso 2: Agregar data de prueba

Use el admin de django para añadir datos de prueba ya que no se incluyen en el repositorio.


### Paso 3: Visualizar endpoints

Para ver las endpoints creados para el reto visite las siguientes rutas:

```
http://127.0.0.1:8000/api/propietarios
http://127.0.0.1:8000/api/edificios
http://127.0.0.1:8000/api/departamentos
```

