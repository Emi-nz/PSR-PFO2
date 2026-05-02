from flask import Flask, request, jsonify
# Importamos bcrypt para hashear contraseñas de forma segura
import bcrypt
import sqlite3

app = Flask(__name__)

#BASE DE DATOS
# Esta función crea la base de datos y la tabla usuarios si no existen.
# Se ejecuta una sola vez al iniciar el servidor.
# IF NOT EXISTS evita que falle si ya fue creada antes.
def init_db():
    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

#REGISTRO DE USUARIOS
# Este endpoint recibe un usuario y contraseña en formato JSON.
# Hashea la contraseña con bcrypt antes de guardarla.
# Si el usuario ya existe, devuelve un error 409.
@app.route("/registro", methods=["POST"])
def registro():
    datos = request.get_json()
    usuario = datos.get("usuario")
    contrasena = datos.get("contraseña")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos"}), 400

    hash = bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt())

    try:
        conn = sqlite3.connect("tareas.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)",
                       (usuario, hash))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 409
    

#LOGIN
# Este endpoint verifica si el usuario existe en la base de datos.
# Compara la contraseña ingresada con el hash guardado usando bcrypt.checkpw.
# Si son correctas devuelve bienvenida, si no devuelve error 401.
@app.route("/login", methods=["POST"])
def login():
    datos = request.get_json()
    usuario = datos.get("usuario")
    contrasena = datos.get("contraseña")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos"}), 400

    conn = sqlite3.connect("tareas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    conn.close()

    if fila and bcrypt.checkpw(contrasena.encode("utf-8"), fila[0]):
        return jsonify({"mensaje": f"Bienvenido, {usuario}!"}), 200
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401
    
#TAREAS
# Este endpoint devuelve una página HTML de bienvenida.
# Solo se accede después de iniciar sesión correctamente desde el cliente.
@app.route("/tareas", methods=["GET"])
def tareas():
    return """
    <html>
        <body>
            <h1>Bienvenido al Sistema de Tareas</h1>
            <p>Estás autenticado correctamente.</p>
        </body>
    </html>
    """

#INICIO
# Inicializamos la base de datos y arrancamos el servidor.
# El modo debug reinicia el servidor automáticamente si modificamos el código.
if __name__ == "__main__":
    init_db()
    app.run(debug=True)