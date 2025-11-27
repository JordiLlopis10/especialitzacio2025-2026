import mysql.connector


# CONEXIÓN SERVER
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="adivinar_numero",
    user="root",
    password="6493")

# OBTENER CURSOR PARA GESTIONAR BBDD
cursor = conexion.cursor()

# CREAMOS LA QUERY
insert_historico = ("INSERT INTO historico "
              "(max_intentos, victoria, puntuacion, dificult) "
              "VALUES (%(max_intentos)s, %(victoria)s, %(puntuacion)s, %(dificult)s)")

dato_historico = {"max_intentos": 40,
           "victoria": True,
           "puntuacion": 50,
           "dificult": 1}

# HACEMOS EL INSERT Y COMMIT
cursor.execute(insert_historico, dato_historico)
conexion.commit()

# CERRAMOS ORDENADAMENTE
cursor.close()
conexion.close()