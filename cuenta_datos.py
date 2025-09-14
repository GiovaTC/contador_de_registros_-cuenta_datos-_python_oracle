import oracledb

# datos de conexion
username = "C##demo_user"
password = "Tapiero123"
dsn = "localhost:1521/orcl"

try:
    #conexion
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    #contar registros en EMPLOYEES
    query = "SELECT COUNT(*) FROM EMPLOYEES"
    cursor.execute(query)
    count = cursor.fetchone()[0]

    print(f"total de registros en EMPLOYEES: {count}")

except oracledb.DatabaseError as e:
    error, = e.args
    print("error en la base de datos: ", error.message)

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()