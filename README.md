# Prueba técnica Lambda Analytics

## Primer punto

A continuación se detallan los pasos para ejecutar el API creada para solucionar el primer punto

1. Se debe crear un entorno virtual con el comando
```bash
python -m venv venv
```
2. Activar el entorno virtual
```bash
source ./venv/bin/activate      # En Linux
./venv/Scripts/activate         # En Windows
```
3. Instalar las librerias necesarias (Django)
```bash
pip install django djangorestframework djangorestframework-simplejwt 
```
4. Luego se debe mover a la carpeta gestion_usuarios
```bash
cd gestion_usuarios
```
5. Inicializar la aplicación
```bash
python manage.py runserver
```

## Segundo y tercer punto

Estos dos punto no se incluyeron en el API, sin embargo, se desarrollo un código en un notebook de jupyter para realizar el scraping y la ETL.
