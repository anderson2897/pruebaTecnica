import psycopg2
from psycopg2 import OperationalError


def conexionDB(query):
    try:
        db_params = {
            'dbname': 'pruebaTecnica',
            'user': 'postgres',
            'password': '123',
            'host': 'localhost',
            'port': '5432'
        }
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        print("queryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryqueryquery")
        print(query)
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except OperationalError as e:
        print("Error operacional", e )


