from flask import Flask, jsonify
from Funciones import getInformationAPI
import psycopg2
from urllib.parse import urlparse

from BaseDatos import conexionDB

app = Flask(__name__)

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJtYWFzIiwibmJmIjoxNjkyMzk0NjQzLCJpc3MiOiJyYnNhcy5jbyIsImNvbXBhbnkiOiIxMDAyIiwiZXhwIjoxNjk0MTE1NDQzLCJ1c2VyIjoiYW5kZXJzb24ucmluY29uIiwiaWF0IjoxNjkyMzg3NDQ0LCJHcnVwb3MiOiJbXCJVbml2ZXJzYWxSZWNoYXJnZXJcIl0ifQ.NO5A6NXTr4Y6POM-Fvh3gmt-_H6VKGm8VYsM0EOaR6ud4Ts3UQk_IXdGM7ytwp7ZWF-2jRz1gEayAT3q9vtWHjraP7LJuzYAKggpEUUKNsOwWpd9kCt8xvt7BjGqtFrO9xIdCaiYaJXE1sg9uVWGR6IT3gcgfuprPeq3GeTNuCxGq_MKWcZ9fBKlIq1JxQ4zCZMYcfHkzgvVBT9Bpuifjsz_du919EPXuf_i0XY8qvhhMCBJdYM28LQd2n1QpSuNvwFW0YLmOkUifAZkGD4iDsALGUEmiIcy3FRZYprU7KSzUKi6muilufQHXG1Y_2bgiccYuxkKykeSneCiX06qHw"

# Configura los parámetros de conexión a la base de datos


@app.route('/consulta', methods=['GET'])
def consultar():
    db_params = {
        'dbname': 'pruebaTecnica',
        'user': 'postgres',
        'password': '123',
        'host': 'localhost',
        'port': '5432'
    }
    url = 'jdbc:postgresql://localhost:5432/pruebaTecnica'
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    consulta = "SELECT * FROM Trazabilidad;"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conn.close()
    return jsonify(resultados)


@app.route('/information', methods=['GET'])
def getInformation():
    card = 1010000008582546
    external_url = f"https://osgqhdx2wf.execute-api.us-west-2.amazonaws.com/card/getInformation/{card}"
    data, status = getInformationAPI(external_url, TOKEN)
    return data, status




@app.route('/balance', methods=['GET'])
def getBalance():
    card = 1010000008582546
    external_url = f"https://osgqhdx2wf.execute-api.us-west-2.amazonaws.com/card/getBalance/{card}"
    data, status = getInformationAPI(external_url, TOKEN)
    return data, status

@app.route('/valid', methods=['GET'])
def valid():
    card = 1010000008582546
    external_url = f"https://osgqhdx2wf.execute-api.us-west-2.amazonaws.com/card/valid/{card}"
    data, status = getInformationAPI(external_url, TOKEN)
    return data, status
if __name__ == '__main__':
    app.run(debug=True)