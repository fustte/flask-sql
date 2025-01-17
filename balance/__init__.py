from flask import Flask
ALMACEN = 1   # 0 - CSV, 1 - DB

app = Flask(__name__)
app.config.from_prefixed_env()

print('***** VARIABLES DE ENTORNO *****')
print('DEBUG', app.config['DEBUG'])
print('APP', app.config['APP'])
print('SECRET KEY', app.config['SECRET_KEY'])
