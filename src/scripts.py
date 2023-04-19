import pyodbc
import hashlib

def obtener_usuario_por_sesion(clave_encriptada):
    # Conectarse a la base de datos
    connection = obtener_conexion()

    # Verificar si la clave encriptada proporcionada corresponde a una sesión activa
    cursor = connection.cursor()
    query = "SELECT usuario_id, nombre FROM sesiones INNER JOIN cuentas ON sesiones.usuario_id = cuentas.id WHERE clave_encriptada = ?;"
    cursor.execute(query, clave_encriptada)
    resultado = cursor.fetchone()

    # Devolver el ID de usuario y el nombre correspondiente a la sesión, o None si la sesión ha caducado
    if resultado is not None:
        usuario_id = resultado[0]
        nombre = resultado[1]
        return [usuario_id, nombre]
    else:
        return None

# Funcion que devuelva la conexion a bdd


def obtener_conexion():
    connection = pyodbc.connect('Driver={MySQL ODBC 8.0 Unicode Driver};'
                                'Server=localhost:3306;'
                                'Database=PyBuys;'
                                'User=root;'
                                'Password=1234;'
                                'Option=3;')
    return connection

# Valida si la sesion es valida


def validate_session(clave):
    response = obtener_usuario_por_sesion(clave)
    if response is not None:
        return True
    else:
        return False

# Metodo que ejecuta el procedimiento almacenado para borrar las sesiones caducadas


def delete_expired_sessions():
    connection = obtener_conexion()
    cursor = connection.cursor()
    cursor.execute('CALL borrar_sesiones_antiguas()')
    connection.commit()
    connection.close()

# Metodo que inicie sesion a traves de la funcion iniciar_sesion en sql de manera segura


def iniciar_sesion(correo, password):
    connection = obtener_conexion()
    cursor = connection.cursor()
    cursor.execute('SELECT iniciar_sesion(?, ?)',correo, password)
    resultado = cursor.fetchone()
    return resultado


# Haz el main y prueba llos metodos
if __name__ == '__main__':
    print(validate_session(iniciar_sesion('a@gmail.com', '1234')))
    delete_expired_sessions()
